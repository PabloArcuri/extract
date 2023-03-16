import { useState, createContext } from "react";

export const UserContext = createContext({});

function UserProvider({children}){
    const [token, setToken] = useState('');
    
    return(
        <UserContext.Provider value={{ token, setToken }}>
            {children}
        </UserContext.Provider>
    )
}

export default UserProvider;