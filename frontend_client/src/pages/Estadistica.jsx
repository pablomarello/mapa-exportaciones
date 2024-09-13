import { CardEstadistica } from "../components/CardEstadistica"
import { Navbar } from "../components/Navbar"
import { Footer } from "../components/Footer"
export const Estadistica = () => {
  return (
    <div>
      <Navbar isTransparent={true}/>
      <div className="pt-[4.5rem]"> {/* Ajusta el margen superior según sea necesario */}
	      <CardEstadistica/>       
      </div>
      <Footer/>
      
    </div>
  )
}
