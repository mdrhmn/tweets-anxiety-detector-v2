// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
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
            meta: [
                {
                    name: "viewport",
                    content: "width=device-width, initial-scale=1",
                },
                {
                    charset: "utf-8",
                },
            ],
            link: [],
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
