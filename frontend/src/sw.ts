/// <reference lib="webworker" />
import { Serwist, CacheFirst, NetworkFirst } from 'serwist';

declare global {
    interface WorkerGlobalScope {
        __WB_MANIFEST: any;
    }
}

declare const self: ServiceWorkerGlobalScope;

const serwist = new Serwist({
    precacheEntries: self.__WB_MANIFEST,
    skipWaiting: true,
    clientsClaim: true,
    navigationPreload: true,
    runtimeCaching: [
        {
            // Cache navigation requests (HTML pages) - always get fresh
            matcher: ({ request }: { request: Request }) => request.mode === 'navigate',
            handler: new NetworkFirst({
                cacheName: 'pages',
            }),
        },
        {
            // Cache everything else (images, CSS, JS, etc.) - serve from cache first
            matcher: () => true,
            handler: new CacheFirst({
                cacheName: 'assets',
            }),
        },
    ],
});

serwist.addEventListeners();

