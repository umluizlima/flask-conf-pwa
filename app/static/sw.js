console.log('Hello from sw.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.4.1/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);
  // workbox.googleAnalytics.initialize();

  workbox.precaching.precacheAndRoute([
    {
      "url": "/",
      "revision": "5"
    },
    {
      "url": "/agenda",
      "revision": "6"
    },
    {
      "url": "/local",
      "revision": "5"
    },
    {
      "url": "/cdc",
      "revision": "5"
    }
  ]);

  workbox.routing.registerRoute(
    /\.(?:js|css)$/,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'static-resources',
    }),
  );

  workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    workbox.strategies.cacheFirst({
      cacheName: 'images',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
        }),
      ],
    }),
  );

  workbox.routing.registerRoute(
    new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
    workbox.strategies.cacheFirst({
      cacheName: 'googleapis',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 30,
        }),
      ],
    }),
  );

} else {
  console.log(`Boo! Workbox didn't load 😬`);
}
