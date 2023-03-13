import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom';

import Home from '../pages/home';
import Register from '../pages/register';


function RoutesApp(){
    return(
        <Routes>
            
            <Route exact path='/' element={ <Home />}/>
            <Route path='/register' element={ <Register /> }/>
            
        </Routes>
       

    )
}

export default RoutesApp;