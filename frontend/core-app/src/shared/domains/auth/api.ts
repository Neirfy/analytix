import { api } from "./../../api/client"

export const authApi = {
  login: (login: string, password: string) =>
    api.post("/auth/login", { login, password }),

  me: () => api.get("/auth/me"),
}