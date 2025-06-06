import { useState } from "react"

export default function MainText() {
  const [count, setCount] = useState(0)

  return (
    <div className="w-full max-w-md px-4 text-center">
      {/* Logo Section */}
      <div className="flex justify-center gap-8 mb-6">
        <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/vite.svg"
            className="w-20 h-20 transition-transform hover:scale-110"
            alt="Vite logo"
          />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/react.svg"
            className="w-20 h-20 transition-transform hover:scale-110"
            alt="React logo"
          />
        </a>
      </div>

      {/* Title */}
      <h1 className="text-4xl font-extrabold mb-6">Vite + React</h1>

      {/* Counter Button */}
      <div className="card bg-gray-800 p-6 rounded-lg shadow-md text-center mb-6">
        <button
          onClick={() => setCount((count) => count + 1)}
          className="px-4 py-2 bg-green-600 rounded hover:bg-green-700 transition-colors"
        >
          count is {count}
        </button>
        <p className="mt-4 text-gray-300">
          Edit <code className="bg-gray-700 px-1 rounded">src/App.jsx</code> and
          save to test HMR
        </p>
      </div>

      {/* Footer Text */}
      <p className="read-the-docs text-sm text-green-400 hover:text-green-300 transition-colors duration-300">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}
