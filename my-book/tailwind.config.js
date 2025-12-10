/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx,md,mdx}"],
  theme: {
    extend: {},
  },
  plugins: [],
  corePlugins: {
    preflight: false, // Docusaurus has its own preflight styles
  },
  blocklist: ['container'], // Avoid conflict with Docusaurus container class if needed, or handle carefully
};
