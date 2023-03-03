import React, { useState, useEffect } from "react";
import axios from "axios";

const Main = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/ops/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Meus Dados</h1>
      {data.map((item) => (
        <div key={item.id}>
          <h2>Título: {item}</h2>
          <p>{item.descricao}</p>
          <p><strong>Autor:</strong> {item.autor}</p>
          <p><strong>Data:</strong> {item.data}</p>
        </div>
      ))} 
    </div>
  );
};

export default Main;