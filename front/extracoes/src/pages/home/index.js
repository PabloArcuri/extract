import './index.css'
import { UserContext } from '../../contexts/user';
import { useContext } from 'react';
import { useNavigate } from "react-router-dom";


function Home() {
  const { token, setToken } = useContext(UserContext);
  let navigate = useNavigate();

 
  function handleLogout(){
    setToken(null);
    navigate('/login'); 
  }



  if (token === '') {
    return (

      <div>
        <h1> Usuário não logado!</h1>
      </div>
    //redirect to login page

    );
  } else {

    return (
      
      
      <div>
        <h1 className='title'>
          Operações do token {token}

        </h1>
        <button onClick={ handleLogout }>Logout</button>

      </div>
      
      
      );
  }
}

export default Home;