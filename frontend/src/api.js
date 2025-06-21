import axios from "axios"
import { ACCESS_TOKEN } from "./constant"


const api = axios.create({
    // it allows to import anything that's specified inside an environment variable file
    baseURL:import.meta.env.VITE_API_URL

})

// inside the arrow function we are going to accept config and what we're going to do is loook in our local storage
// and see if we have access token  if we do we're going to add that as an authorization header to our request otherwise 
// there's nothing that we need to do cause  we dont have a header


api.interceptors.request.use(
    (config) =>{
const token = localStorage.getItem(ACCESS_TOKEN);
if(token) {
    config.headers.Authorization = `Bearer ${token}`
}
return config
    },
    (error) =>{
        return Promise.reject(error)
    }

)


export default api