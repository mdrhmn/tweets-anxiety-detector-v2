// References:
// https://stackoverflow.com/questions/69021542/how-to-resolve-parsing-error-this-experimental-syntax-requires-enabling-one-of
// https://github.com/weicheng2138/nuxt3-eslint-starter
module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    commonjs: true,
    es2021: true,
  },

  rules: {
    // Set EOL to auto
    "prettier/prettier": ["error", { endOfLine: "auto" }],

    // Prevent unused vars
    "vue/no-unused-vars": "error",
    // "no-unused-expressions": "off",

    // Only allow pascal casing
    "vue/component-name-in-template-casing": ["error", "PascalCase"],

    // Disable rule
    "vue/multi-word-component-names": "off",

    // Console and debugger
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",

    // Only allow double quotes
    quotes: ["error", "double", { allowTemplateLiterals: true }],
    semi: [2, "always"],

    // No indents
    indent: "off",

    // Based on the operating system, it will take appropriate line endings.
    // Reference: https://stackoverflow.com/questions/37826449/expected-linebreaks-to-be-lf-but-found-crlf-linebreak-style
    "linebreak-style": [
      "error",
      process.platform === "win32" ? "windows" : "unix",
    ],

    // New line at last line
    "eol-last": "error",

    // No tabs
    "no-tabs": "error",
  },

  extends: [
    // eslint:recommended is ESLint"s inbuilt "recommended" config - it turns on a small, sensible set of rules which lint for well-known best-practices.
    "eslint:recommended",

    // Settings and rules to enable correct ESLint parsing.
    "plugin:vue/base",

    // base, plus rules to prevent errors or unintended behavior.
    "plugin:vue/vue3-essential",

    // Tells ESLint to incorporate Vue specific rules (e.g you cannot use v-model on divs)
    "plugin:vue/vue3-recommended",

    // vue/recommended + plus rules to considerably improve code readability and/or dev experience.
    "plugin:vue/vue3-strongly-recommended",

    // Nuxt
    "plugin:nuxt/base",
    "plugin:nuxt/recommended",

    // plugin:@typescript-eslint/recommended is our "recommended" config - it"s similar to eslint:recommended, except it turns on TypeScript-specific rules from our plugin.
    "plugin:@typescript-eslint/recommended",
    "@nuxtjs/eslint-config-typescript",

    // Turns on both eslint-plugin-prettier and eslint-config-prettier which tells
    // ESLint to treat prettier errors as linting errors and disable certain rules
    // that interfere with prettier (should prevent weird loops).
    "plugin:prettier/recommended",
    "prettier",
  ],

  globals: {
    $nuxt: true,
  },

  parser: "vue-eslint-parser",
  parserOptions: {
    ecmaVersion: "latest",
    parser: "@typescript-eslint/parser",
    requireConfigFile: false,
    // Allows for the use of imports
    sourceType: "module",
  },
};
