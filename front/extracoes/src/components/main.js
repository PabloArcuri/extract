import React, { useContext, useState } from "react";

import { UserContext } from "../contexts/user";


function Main() {
    const { alunos, setAlunos } = useContext(UserContext)
    const {btnview, setBntview} = useState('false')

    function edita(e){
        setAlunos(e.target.value);
    }
    
    return ( 
        <div>
            <input type="text" value={alunos} onChange= {edita}/> 
            <button >  Salvar </button>
        </div>
     );
     
     
}

export default Main;
