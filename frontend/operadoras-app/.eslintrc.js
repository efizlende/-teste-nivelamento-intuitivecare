module.exports = {
    root: true,
    env: {
      browser: true,
      node: true,
    },
    parserOptions: {
      parser: "@babel/eslint-parser",
      requireConfigFile: false,
    },
    extends: [
      "eslint:recommended",
      "plugin:vue/vue3-recommended" // Se estiver usando Vue 3
    ],
    rules: {
      "vue/multi-word-component-names": "off",
      "no-console": "warn",
      "no-debugger": "warn",
    },
  };
  