import { useState } from 'react'
import { BrowserRouter, Routes,Route,Navigate } from 'react-router-dom';
import Login from "./pages/Login"
import Register from './pages/Register';
import Notfound from './pages/Notfound';
import ProtectedRoute from './components/ProtectedRoute';
import "../src/styles/Form.css"



function Logout(){
  localStorage.clear()
  return <Navigate to = "/login" />
}

// if someone is registering i first want to clear local storage so i don't end up submitting access token  to register route where i can potentially get error

function RegisterAndLogout(){
  localStorage.clear()
  return <Register />
}
function App() {
 
  return (
    <>
         <BrowserRouter>
      <Routes>
        {/* <Route
          path = "/"
          element = {
            <ProtectedRoute>
              <Home/>
            </ProtectedRoute>
          }
        /> */}
        <Route path = "/login" element = {<Login />} />
        <Route path = "/logout" element = {<Logout />} />
                <Route path = "/register" element = {<RegisterAndLogout />} />
                        <Route path = "*" element = {<Notfound/>} />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
