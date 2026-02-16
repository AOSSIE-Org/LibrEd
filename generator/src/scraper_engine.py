import logging
import asyncio
from playwright.async_api import async_playwright
from generator.src.config import GATE_ACADEMY_URL, RAW_DATA_DIR
import os
import requests

logger = logging.getLogger(__name__)

class ScraperEngine:
    def __init__(self):
        self.browser = None
        self.context = None

    async def initialize(self):
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()

    async def close(self):
        if self.browser:
            await self.browser.close()

    async def download_file(self, url, dest_path):
        if os.path.exists(dest_path):
            logger.info(f"File already exists: {dest_path}")
            return
        
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        try:
            resp = requests.get(url, stream=True)
            resp.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"Downloaded: {dest_path}")
        except Exception as e:
            logger.error(f"Failed to download {url}: {e}")

    async def run(self, stream_code):
        logger.info(f"Starting scrape for {stream_code}")
        await self.initialize()
        
        # Resolve Alias
        from generator.src.config import STREAM_ALIASES
        stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
        
        # 1. Syllabus & PYQs via run_for_stream
        await self.run_for_stream(stream_code, stream_alias)

    async def find_pdf_links(self, stream_slug, year):
        # Logic to find PDF links based on stream and year
        # Pattern derived from browser subagent: 
        # PY Papers: https://www.gateacademy.co.in/py-papers/{stream_slug}/{year}
        # Iterate years, then go to specific page, then find storage.googleapis.com link
        
        # Example URL: https://www.gateacademy.co.in/py-papers/computer-science-information-technology/2024-M
        # We need to crawl the 'py-papers' page to find available years/variants for the stream first?
        # Or just try constructing likely URLs? The browser subagent saw "2024-M", "2021-N" etc.
        # Better to visit the stream page `py-papers` and find links containing the stream slug.

        paper_url_base = f"{GATE_ACADEMY_URL}/py-papers"
        # We might need to visit the main py-papers page to find the specific stream card/section if we didn't know the slug,
        # but we have the slug.
        # Does /py-papers/{stream_slug} exist?
        # Let's assume we visit the stream specific section if it exists, or the main page.
        
        # Strategy:
        # 1. Visit main py-papers page.
        # 2. Find links that look like /py-papers/{stream_slug}/{year_variant}
        # 3. Visit each of those.
        # 4. Extract PDF link.
        
        page = await self.context.new_page()
        await page.goto(paper_url_base)
        
        # Find all year links for this stream
        # Selector for links containing relevant slug
        links = await page.evaluate(f"""(slug) => {{
            const anchors = Array.from(document.querySelectorAll('a'));
            return anchors
                .map(a => a.href)
                .filter(href => href.includes('/py-papers/' + slug + '/'));
        }}""", stream_slug)
        
        pdf_map = {} # year_variant -> pdf_url
        
        unique_links = set(links)
        logger.info(f"Found {len(unique_links)} potential paper pages for {stream_slug}")

        for link in unique_links:
            variant = link.split('/')[-1] # e.g. 2024-M
            logger.info(f"Inspecting {variant} at {link}")
            try:
                await page.goto(link, timeout=30000)
                # Helper to find Google Storage PDF
                pdf_url = await page.evaluate("""() => {
                    const scripts = Array.from(document.querySelectorAll('script'));
                    for (const s of scripts) {
                         const match = s.textContent.match(/https?:\\/\\/[^"']+\\.pdf/);
                         if (match) return match[0];
                    }
                    const iframes = Array.from(document.querySelectorAll('iframe'));
                    for (const i of iframes) if (i.src.endsWith('.pdf')) return i.src;
                    
                    const embeds = Array.from(document.querySelectorAll('embed'));
                    for (const e of embeds) if (e.src.endsWith('.pdf')) return e.src;
                    
                    return null;
                }""")
                
                if pdf_url:
                    pdf_map[variant] = pdf_url
                    logger.info(f"Found PDF for {variant}: {pdf_url}")
            except Exception as e:
                logger.error(f"Error scraping {link}: {e}")
                
        await page.close()
        return pdf_map

    async def find_syllabus_pdf(self, stream_slug):
        # URL Logic: https://www.gateacademy.co.in/syllabus/{stream_slug}
        # And then click on the year link e.g., .../2025
        base_url = f"{GATE_ACADEMY_URL}/syllabus/{stream_slug}"
        logger.info(f"Inspecting Syllabus at {base_url}")
        
        page = await self.context.new_page()
        try:
            await page.goto(base_url, timeout=30000)
            
            # 1. Find the specific year page (e.g., .../2025)
            year_link = await page.evaluate(f"""(slug) => {{
                const anchors = Array.from(document.querySelectorAll('a'));
                // Look for links containing /syllabus/slug/20..
                const matches = anchors
                    .map(a => a.href)
                    .filter(href => href.includes('/syllabus/' + slug + '/'));
                // Return the matching link (first one usually fine)
                return matches.length > 0 ? matches[0] : null; 
            }}""", stream_slug)
            
            if year_link:
                logger.info(f"Found Syllabus Year Page: {year_link}")
                await page.goto(year_link, timeout=30000)
            
            # 2. Find the PDF link on the page
            pdf_url = await page.evaluate("""() => {
                const scripts = Array.from(document.querySelectorAll('script'));
                for (const s of scripts) {
                     const match = s.textContent.match(/https?:\\/\\/[^"']+\\.pdf/);
                     if (match) return match[0];
                }
                const iframes = Array.from(document.querySelectorAll('iframe'));
                for (const i of iframes) if (i.src.endsWith('.pdf')) return i.src;
                
                const embeds = Array.from(document.querySelectorAll('embed'));
                for (const e of embeds) if (e.src.endsWith('.pdf')) return e.src;
                
                const anchors = Array.from(document.querySelectorAll('a'));
                for (const a of anchors) if (a.href.endsWith('.pdf')) return a.href;

                return null;
            }""")
            
            return pdf_url
        except Exception as e:
            logger.error(f"Error scraping syllabus {base_url}: {e}")
            return None
        finally:
            await page.close()

    async def run_for_stream(self, stream_code, stream_alias):
        logger.info(f"Starting deep scrape for {stream_code} (Alias: {stream_alias})")
        
        stream_dir = os.path.join(RAW_DATA_DIR, stream_alias)
        
        # 1. Syllabus (Always download)
        syllabus_url = await self.find_syllabus_pdf(stream_code)
        if syllabus_url:
            logger.info(f"Found Syllabus PDF: {syllabus_url}")
            dest = os.path.join(stream_dir, "syllabus.pdf")
            await self.download_file(syllabus_url, dest)
        else:
            logger.warning(f"No syllabus found for {stream_code}")

        # 2. PYQ Papers (Always download)
        pdf_links = await self.find_pdf_links(stream_code, None) # year is None meant 'all'
        
        for variant, url in pdf_links.items():
            # Save to raw/stream_alias/variant.pdf
            dest = os.path.join(stream_dir, f"{variant}.pdf")
            await self.download_file(url, dest)
