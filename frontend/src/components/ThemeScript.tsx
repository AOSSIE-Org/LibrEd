import { HeadContent } from '@tanstack/react-router'

export function ThemeScript() {
    return (
        <HeadContent>
            <script
                dangerouslySetInnerHTML={{
                    __html: `
            (function() {
              try {
                var theme = localStorage.getItem('dont-compete-theme') || 'dracula';
                document.documentElement.setAttribute('data-theme', theme);
              } catch (e) {}
            })();
          `,
                }}
            />
        </HeadContent>
    )
}
