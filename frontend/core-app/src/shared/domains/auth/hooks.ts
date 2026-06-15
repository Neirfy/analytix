import { useState } from "react"
import { authModel } from "./model"

export function useAuth() {
  const [loading, setLoading] = useState(false)

  const login = async (login: string, password: string) => {
    setLoading(true)

    try {
      return await authModel.login(login, password)
    } finally {
      setLoading(false)
    }
  }

  return { login, loading }
}