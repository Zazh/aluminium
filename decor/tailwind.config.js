/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./catalog.html",
    "./product.html",
    "./categorys.html",
    "./article.html",
    "./articles-list.html",
    "./contacts.html",
    "./sales-points.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        '24': 'repeat(24, minmax(0, 1fr))',
      }
    }
  },
  plugins: [],
} 