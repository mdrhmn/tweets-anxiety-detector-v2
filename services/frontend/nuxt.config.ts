import config from "./config";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiURL: process.env.API_URL || "http://127.0.0.1:8000/predict-lime/",
    },
  },

  modules: ["@nuxt/image-edge"],

  imports: {
    dirs: [
      "stores",
      // Scan top-level modules
      "composables",
      // ... or scan modules nested one level deep with a specific name and file extension
      "composables/*/index.{ts,js,mjs,mts}",
      // ... or scan all modules within given directory
      "composables/**",
    ],
  },

  app: {
    head: {
      title: `Tweets Anxiety Predictor`,
      htmlAttrs: {
        lang: "en",
      },
      meta: [
        {
          name: "viewport",
          content: "width=device-width, initial-scale=1",
        },
        {
          charset: "utf-8",
        },
        {
          hid: "description",
          name: "description",
          content:
            "A single-page application (SPA) developed using Nuxt 3 and FastAPI for predicting the anxiety probability of a given tweet (or any text prompt limited to max. 280 characters).",
        },
        {
          hid: "title",
          name: "title",
          content: `Tweets Anxiety Predictor`,
        },
        {
          // hid: 'author',
          name: "author",
          content: config.name,
        },
        {
          // hid: "og:type",
          property: "og:type",
          content: "website",
        },
        {
          hid: "og:url",
          property: "og:url",
          content: `https://${config.domain}`,
        },
        {
          hid: "og:title",
          property: "og:title",
          content: `Tweets Anxiety Predictor`,
        },
        {
          hid: "og:description",
          property: "og:description",
          content:
            "A single-page application (SPA) developed using Nuxt 3 and FastAPI for predicting the anxiety probability of a given tweet (or any text prompt limited to max. 280 characters).",
        },
        {
          hid: "og:image",
          property: "og:image",
          content: `https://${config.domain}/img/sentiment-analysis-of-twitter.png`,
        },
        {
          hid: "twitter:image",
          property: "twitter:image",
          content: `https://${config.domain}/img/sentiment-analysis-of-twitter.png`,
        },
        {
          hid: "twitter:card",
          name: "twitter:card",
          content: "summary_large_image",
        },
        {
          hid: "twitter:site",
          name: "twitter:site",
          content: "@" + config.social.twitter,
        },
        {
          hid: "twitter:creator",
          name: "twitter:creator",
          content: "@" + config.social.twitter,
        },
        {
          hid: "twitter:url",
          property: "twitter:url",
          content: `https://${config.domain}`,
        },
        {
          hid: "twitter:title",
          property: "twitter:title",
          content: "Tweets Anxiety Predictor",
        },
        {
          hid: "twitter:description",
          property: "twitter:description",
          content:
            "A single-page application (SPA) developed using Nuxt 3 and FastAPI for predicting the anxiety probability of a given tweet (or any text prompt limited to max. 280 characters).",
        },
      ],
      link: [
        {
          rel: "apple-touch-icon",
          type: "image/png",
          href: `https://${config.domain}/img/apple-touch-icon.png`, // If Icon is inside @/assets/ folder or available at '/...'
        },
      ],
      style: [],
      script: [],
      noscript: [],
    },
  },

  css: ["~/assets/css/main.css"],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
});
