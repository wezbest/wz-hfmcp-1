import { useState } from "react"

export default function MainText() {
  const [count, setCount] = useState(0)

  return (
    <div className="">
      {/* Logo Section */}
      <div className="flex justify-center gap-12 mb-6">
        <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/vite.svg"
            className="w-24 h-24 logo transition-transform hover:scale-110"
            alt="Vite logo"
          />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/vite.svg"
            className="w-24 h-24 logo react transition-transform hover:scale-110"
            alt="React logo"
          />
        </a>
      </div>

      {/* Title */}
      <h1 className="text-4xl font-bold ">Vite </h1>

      {/* Counter Button */}
      <div className="card bg-gray-800 p-6 rounded-lg shadow-md w-full max-w-sm text-center mb-4">
        <button
          onClick={() => setCount((count) => count + 1)}
          className="px-4 py-2 bg-blue-600 rounded hover:bg-blue-700 transition"
        >
          count is {count}
        </button>
        <p className="mt-4 text-gray-300">
          Edit <code className="bg-gray-700 px-1 rounded">src/App.jsx</code> and
          save to test HMR
        </p>
      </div>

      {/* Footer Text */}
      <p className="read-the-docs text-sm text-gray-400 hover:text-white transition-colors duration-300 text-center">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}
