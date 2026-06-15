import { useState } from "react"

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{
      padding: 20,
      borderRadius: 12
    }}>
      <h2>Chat App (Remote)</h2>

      <p>Это микрофронт из chat-app</p>

      <button onClick={() => setCount(c => c + 1)}>
        count: {count}
      </button>
    </div>
  )
}