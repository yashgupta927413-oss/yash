import { defineConfig } from 'vite';

// In dev, Vite serves the homepage; everything else proxies to Django on :8000.
// In production, nginx routes: / → built Vite static, /blog/* /api/* /admin/* /sitemap.xml /robots.txt → Django.
export default defineConfig({
  // Django reads dist/.vite/manifest.json to link the hashed CSS/JS from the
  // server-rendered blog and service pages. See backend/website/assets.py.
  build: { manifest: true },
  server: {
    proxy: {
      '/api': { target: 'http://127.0.0.1:8000', changeOrigin: true },
      '/admin': { target: 'http://127.0.0.1:8000', changeOrigin: true },
      '/sitemap.xml': { target: 'http://127.0.0.1:8000', changeOrigin: true },
      '/robots.txt': { target: 'http://127.0.0.1:8000', changeOrigin: true },
      // Blog + service pages: server-rendered by Django.
      '/blog': { target: 'http://127.0.0.1:8000', changeOrigin: true },
      '/services': { target: 'http://127.0.0.1:8000', changeOrigin: true },
    },
  },
});
