import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import "./App.css"
import App from "./App.jsx"

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <div className="min-h-screen bg-slate-950 ">
      <App />
    </div>
  </StrictMode>
)
