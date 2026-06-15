import { authApi } from "./api"

export const authModel = {
  async login(login: string, password: string) {
    const res = await authApi.login(login, password)

    localStorage.setItem("token", res.data.token)

    return res.data
  },

  logout() {
    localStorage.removeItem("token")
  },
}