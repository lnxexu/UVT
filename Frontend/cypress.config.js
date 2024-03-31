import { defineConfig } from "cypress";

export default defineConfig({
<<<<<<< HEAD
  component: {
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },

  component: {
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },

=======
>>>>>>> 18134f7757a787893fc91204cd933c8952f79895
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
