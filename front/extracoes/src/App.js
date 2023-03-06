import Main from "./components/main";
import UserProvider from "./contexts/user";

function App() {
  
  return (
    <UserProvider>
      <div className="App">
        <Main />
      </div>
    </UserProvider>
  );
}

export default App;
