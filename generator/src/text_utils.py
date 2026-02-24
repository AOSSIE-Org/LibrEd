
import re

def normalize_subtopic(name):
    """Normalizes subtopic name to reduce duplicates."""
    if not name: return ""
    
    # 1. Lowercase
    name = name.lower()
    
    # 2. Fix common typos
    typos = {
        'complier': 'compiler',
        'computational': 'computation',
    }
    for typo, fix in typos.items():
        name = name.replace(typo, fix)

    # 3. Replace symbols and separators with spaces
    name = name.replace('&', ' and ').replace('+', ' plus ')
    name = re.sub(r'[/\-_]', ' ', name)
    
    # 4. Remove punctuation (keep alphanumeric and spaces)
    name = re.sub(r'[^\w\s]', '', name)
    
    # 5. Remove 'section-<no.>-' prefixes
    name = re.sub(r'^section\s*\d+\s*', '', name)
    
    # 6. Collapse multiple spaces and strip
    name = ' '.join(name.split())
    
    # 6. Remove trailing noise words and symbols
    # We do this iteratively as removing one might expose another (e.g., "Algorithm and &")
    noise_words = {'and', 'system', 'systems', 'plus', 's'}
    
    while True:
        words = name.split()
        if not words: break
        
        changed = False
        last_word = words[-1]
        
        # Check if last word is a noise word
        if last_word in noise_words:
            words.pop()
            changed = True
        
        # Aggressive plural removal (if not a stop word protected ending)
        elif last_word.endswith('s') and not any(last_word.endswith(x) for x in ['ss', 'is', 'us', 'as']):
            if len(last_word) > 3:
                words[-1] = last_word[:-1]
                changed = True
        
        if not changed:
            break
        name = ' '.join(words)
        
    return name.strip()

def slugify(text, normalize=True):
    """Converts text to a slug, optionally normalizing it first."""
    if normalize:
        text = normalize_subtopic(text)
    
    res = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    if len(res) > 80:
        res = res[:80].strip('-')
    return res
