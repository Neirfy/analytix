import { userApi } from "./api"

export const userModel = {
  async list() {
    const res = await userApi.getAll()
    return res.data
  },
}