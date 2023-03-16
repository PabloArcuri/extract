import { Route, Routes } from 'react-router-dom';

import Home from '../pages/home';
import Register from '../pages/register';
import Login from '../pages/login';
import UserProvider from '../contexts/user';



function RoutesApp(){
    return(
        
       <UserProvider>

       <Routes>
            
            <Route exact path='/' element={ <Home />}/>
            <Route path='/register' element={ <Register /> }/>
            <Route path='/login' element={ <Login /> }/>
            
        </Routes>
       
       </UserProvider>

    )
}

export default RoutesApp;