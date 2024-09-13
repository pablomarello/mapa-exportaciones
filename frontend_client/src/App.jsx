import { AppRouter } from './AppRouter';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {Productos} from './pages/Productos';
import {Inicio} from './pages/Inicio';
import { Navigation } from './components/Navigation';
import { Navbar } from './components/Navbar';
import { Trivia } from './pages/Trivia';
import { Map } from './pages/Map';
import { Exportaciones } from './pages/Exportaciones';
import { CardEstadistica } from './components/CardEstadistica';
import { Estadistica } from './pages/Estadistica';


function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path='/' Component={Inicio}/>
        <Route path='/productos' Component={Productos}/>
        <Route path='/mapa' Component={Map} />
        <Route path='/trivia' Component={Trivia} />
        <Route path="/exportaciones" element={<Exportaciones/>}/>
        <Route path='/estadistica' element={<Estadistica/>}/>
      </Routes>
    </Router>
    {/* <AppRouter/> */}
    {/* <Navbar/>
    <BrowserRouter>
    <Navigation/>
    <Routes>
      <Route path="/" element={<Navigate to="/index"/>}/>
      <Route path="/index" element={<Inicio/>}/>
      <Route path="/productos" element={<Productos/>}/>
    </Routes>
    </BrowserRouter> */}
    </>
  )
}

export default App
