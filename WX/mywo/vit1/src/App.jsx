import "./App.css"
import Form1 from "./compo/form1"
import MainText from "./compo/maintext"

function App() {
  return (
    <>
      <div className="flex items-center justify-between min-h-screen bg-slate-950 text-green-500 p-8">
        {/* Left Side - MainText */}
        <div className="md:w-1/2 w-full flex items-center justify-center mb-6 md:mb-0 md:pr-4">
          <div className="w-full max-w-lg">
            <MainText />
          </div>
        </div>

        {/* Right Side - Form1 */}
        <div className="md:w-1/2 w-full flex items-center justify-center md:pl-4">
          <div className="w-full max-w-md">
            <Form1 />
          </div>
        </div>
      </div>
    </>
  )
}

export default App
