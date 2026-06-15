import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Login() {
  const [login, setLogin] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  const onSubmit = () => {
    if (!login || !password) return

    localStorage.setItem("token", "fake-token")
    navigate("/")
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100 dark:bg-gray-900
    bg-[url('/bg.png')] bg-cover bg-no-repeat"
    >
      
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg dark:bg-gray-800">
        
        <h1 className="mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          Login
        </h1>

        <div className="space-y-4">
          <input
            className="w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-gray-900 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
            placeholder="login"
            value={login}
            onChange={(e) => setLogin(e.target.value)}
          />

          <input
            className="w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-gray-900 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
            placeholder="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            onClick={onSubmit}
            className="w-full rounded-lg bg-blue-600 py-3 font-medium text-white transition hover:bg-blue-700 active:scale-[0.98]"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  )
}