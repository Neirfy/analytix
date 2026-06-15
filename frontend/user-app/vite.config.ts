import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { federation } from "@module-federation/vite"

// https://vite.dev/config/

export default defineConfig({
  base: "/",
  plugins: [
    react(),
    federation({
      name: "user",
      filename: "remoteEntry.js",
      dts: false,
      exposes: {
        "./App": "./src/App.tsx", 
      },
      shared: {
        react: {
          singleton: true,
        },
        "react-dom": {
          singleton: true,
        },
      },
    }),
  ],
  resolve: {
    dedupe: ["react", "react-dom"],
  },
  build: {
    target: "esnext",
    assetsDir: "assets",
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        entryFileNames: "remoteEntry.js",
        // format: "esm",
      },
    },

  },
  server: {
    host: "0.0.0.0",
    port: 3001,
    strictPort: true,
    cors: true,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
      "Access-Control-Allow-Methods": "*",
    }
  },
})
