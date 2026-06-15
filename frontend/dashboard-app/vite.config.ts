import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { federation } from "@module-federation/vite"

// https://vite.dev/config/

export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "dashboard",
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
        format: "esm",
      },
    },

  },
  server: {
    port: 3002,
    strictPort: true,
    cors: true
  },
})
