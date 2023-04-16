import './App.css';
import Home from './home'
import Sobre from './sobre'
import { Routes, Route, Link } from 'react-router-dom'
function App() {
  return (
    <>
      <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
        <Link to="/">Home</Link>
        <Link to="/sobre"style={{margin: "0 10px"}}>sobre nos </Link>
      </div>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/sobre" element={<Sobre />} />
      </Routes>
    </>
  );
}

export default App;
