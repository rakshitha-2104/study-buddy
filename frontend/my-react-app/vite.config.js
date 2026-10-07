import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Forwards /api calls to the Flask server so the browser sees a single origin.
export default defineConfig({
  plugins: [react()],
  server: { proxy: { "/api": "http://localhost:5000" } },
});