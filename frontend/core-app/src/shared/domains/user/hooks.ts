import { useEffect, useState } from "react"
import { userModel } from "./model"

export function useUsers() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    userModel.list().then(setUsers)
  }, [])

  return { users }
}