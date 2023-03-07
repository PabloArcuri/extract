import { Router, Route, Routes } from 'react-router-dom';


import Home from '../pages/home';
import Register from '../pages/register';


function RoutesApp(){
    return(
        <Routes>
            <Route path='/' element={ <Home/> }/>
            <Route path='/register' element={ <Register/> }/>
        </Routes>

    )
}

export default RoutesApp;