import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import { federation } from "@module-federation/vite"

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "VITE_")

  return {

  plugins: [react(),
  federation({
      name: "core",
      dev: {
        disableLiveReload: false,
        disableHotTypesReload: true,
      },
      remotes: {
        user: {
          type: "module",
          name: "user",
          entry: env.VITE_USER_REMOTE,
        },
        // profile: {
        //   // type: "module",
        //   name: "profile",
        //   entry: env.VITE_PROFILE_REMOTE,
        // },
        // calendar: {
        //   // type: "module",
        //   name: "calendar",
        //   entry: env.VITE_CALENDAR_REMOTE,
        // },
        // dashboard: {
        //   // type: "module",
        //   name: "dashboard",
        //   entry: env.VITE_DASHBOARD_REMOTE,
        // },
        // chat: {
        //   // type: "module",
        //   name: "chat",
        //   entry: env.VITE_CHAT_REMOTE,
        // },
        // reports: {
        //   // type: "module",
        //   name: "reports",
        //   entry: env.VITE_REPORTS_REMOTE,
        // },
        
      },
      dts: false,
      runtime: true,
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
  server: {
    host: "0.0.0.0",
    port: 3000,
    strictPort: true,
  },
  optimizeDeps: {
    include: ["react", "react-dom"],
  },
}
})
