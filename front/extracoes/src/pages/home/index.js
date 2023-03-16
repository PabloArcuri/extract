import './index.css'
import { UserContext } from '../../contexts/user';
import { useContext } from 'react';


function Home() {
  const { token, setToken } = useContext(UserContext);

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

      </div>
    );
  }
}

export default Home;