import { createContext, useState } from "react"

const Context = createContext()

export default Context

export const ContextProvider = ({ children }) => {
    const [authtoken,setauthtoken] = useState(null)
    const [user,setuser] = useState(null)
    const [invert, setinvert] = useState(false)
    const [Contests, setContests] = useState([])
    const [nexturl, setnexturl] = useState('http://127.0.0.1:8000/api/v1/ListAllContest')
    const openoffcanvas = () =>{
		
        document.getElementById('offcanvas').classList.toggle('smenu1')
    }
    const ContextData =  {
        openoffcanvas:openoffcanvas,
        authtoken:authtoken,
        setauthtoken:setauthtoken,
        user:user,
        setuser:setuser,
        invert:invert,
        setinvert:setinvert,
        Contests:Contests,
        setContests:setContests,
        nexturl:nexturl,
        setnexturl:setnexturl,
    }
    return (
        <Context.Provider value={ContextData}>
            {children}
        </Context.Provider>
    )

}