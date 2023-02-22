module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    commonjs: true,
    es2021: true
  },
  extends: [
    // "@babel/core",
    // "@babel/preset-env",

    // Configures ESLint to use some default best-practice rules like getters always need to return a value
    "eslint:recommended",

    // Turns on both eslint-plugin-prettier and eslint-config-prettier which tells
    // ESLint to treat prettier errors as linting errors and disable certain rules
    // that interfere with prettier (should prevent weird loops).
    // "prettier",
    // "plugin:prettier/recommended",
    // "eslint-config-prettier",

    // Settings and rules to enable correct ESLint parsing.
    "plugin:vue/base",

    // base, plus rules to prevent errors or unintended behavior.
    "plugin:vue/vue3-essential",

    // Tells ESLint to incorporate Vue specific rules (e.g you cannot use v-model on divs)
    "plugin:vue/vue3-recommended",

    // vue/recommended + plus rules to considerably improve code readability and/or dev experience.
    "plugin:vue/vue3-strongly-recommended",

    // "plugin:nuxt/base",
    // "plugin:nuxt/recommended",
    // TypeScript lint
    "plugin:@typescript-eslint/recommended",
    "@nuxtjs/eslint-config-typescript"
  ],
  rules: {
    // Prevent unused vars
    "vue/no-unused-vars": "error",

    // Only allow pascal casing
    "vue/component-name-in-template-casing": ["error", "PascalCase"],

    // Disable rule
    "vue/multi-word-component-names": "off",

    // Console and debugger
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",

    // Set EOL to auto
    // "prettier/prettier": ["error", { endOfLine: "auto" }],

    // Only allow double quotes
    quotes: ["error", "double", { allowTemplateLiterals: true }],
    semi: "error",

    // Based on the operating system, it will take appropriate line endings.
    // Reference: https://stackoverflow.com/questions/37826449/expected-linebreaks-to-be-lf-but-found-crlf-linebreak-style
    "linebreak-style": [
      "error",
      process.platform === "win32" ? "windows" : "unix"
    ],

    // New line at last line
    "eol-last": "error",

    // No tabs
    "no-tabs": "error"
  },

  globals: {
    $nuxt: true
  },

  // parser: "@typescript-eslint/parser",
  // parser: "@babel/eslint-parser",
  parserOptions: {
    ecmaVersion: 12,
    parser: "@babel/eslint-parser",
    requireConfigFile: false,
    sourceType: "module"
  }
}
