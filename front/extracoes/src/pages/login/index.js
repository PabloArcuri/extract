import React, { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from '../../contexts/user';
import axios from 'axios';



function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const { token, setToken } = useContext(UserContext);
    const url = 'http://localhost:8000/api/token/';
    let navigate = useNavigate();

    function handleLogin(e) {
        e.preventDefault();
        if (username !== '' && password !== '') {
            console.log(username, password);

            axios.post(url,{
                'username': username,
                'password': password
            }).then(
                function (response) {
                    
                    setToken(response.data.access);
                    
                    navigate('/');
                    console.log(token)
                }).catch(
                function (error) {
                    console.log('error');

                })
            }
        
        
    
        else {
        alert("Preencha todos os dados!")
    }
}

return (
    <div className="container">
        <h1 className='title'>
            Faça seu login

        </h1>
        <h2 className='subtitle'> Preencha seus dados</h2>
        <form className='loginForm' onSubmit={handleLogin}>
            <input type="text" name="username" placeholder="Username" value={username} required
                onChange={(e) => setUsername(e.target.value)} />
            <input type="password" name="password" placeholder="Password" value={password} required
                onChange={(e) => setPassword(e.target.value)} />
            <button> Entrar</button>

        </form>
        <div className="subDiv">
            <h3> <Link to='/' className="link">Solicitar acesso </Link></h3>

        </div>
    </div>
);
  
     
}

export default Login;