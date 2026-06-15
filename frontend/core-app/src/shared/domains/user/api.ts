import { api } from "./../../api/client"

export const userApi = {
  getAll: () => api.get("/users"),
  getById: (id: string) => api.get(`/users/${id}`),
}