import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { AreaChart, Area, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Custom Tooltip for the AreaChart (Productos por rubro)
const CustomTooltipRubro = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className="custom-tooltip" style={{ backgroundColor: '#fff', padding: '10px', border: '1px solid #ccc' }}>
        <p className="label">{`Rubro: ${label}`}</p>
        <p>{`Total de Productos: ${payload[0].value}`}</p>
      </div>
    );
  }
  return null;
};

// Custom Tooltip for the BarChart (FOB Dólar acumulado por año)
const CustomTooltipFob = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    const formatter = new Intl.NumberFormat('es-ES', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2
    });

    return (
      <div className="custom-tooltip" style={{ backgroundColor: '#fff', padding: '10px', border: '1px solid #ccc' }}>
        <p className="label">{`Año: ${label}`}</p>
        <p>{`Total FOB Dólar: ${formatter.format(payload[0].value)}`}</p>
      </div>
    );
  }
  return null;
};

export const CardEstadistica = () => {
  const [productosData, setProductosData] = useState([]);
  const [fobData, setFobData] = useState([]);
  const [selectedYear, setSelectedYear] = useState(2023);

  const rubrosMap = {
    1: 'Minería',
    2: 'Olivícola',
    3: 'Citrícola',
    4: 'Cereales y Oleagionsas',
    5: 'Legumbres',
    6: 'Hortalizas',
    7: 'Textil',
    8: 'Conservas',
    9: 'Vitivinícola',
    10: 'Frutos Secos',
    11: 'Alimenticios',
    12: 'Salud',
    13: 'Bebidas',
    14: 'Otros',
    // Mapea todos los IDs a sus nombres
  };

  // Función para obtener los productos y contar los productos por rubro
  
  
  const fetchProductos = async () => {
    try {
      const response = await axios.get('http://localhost:8000/exportaciones/api/exportaciones/');
      const productos = response.data; // Asegúrate de que 'productos' está definido aquí
      console.log('Productos de la API:', productos);

      // Filtrar productos por año seleccionado y procesar datos
      const productosPorRubro = productos
        .filter(producto => selectedYear === null || producto.año === selectedYear)
        .reduce((acc, producto) => {
          const rubroId = producto.producto.rubro;
          const rubroNombre = rubrosMap[rubroId] || 'Desconocido'; // Mapea el ID al nombre
          if (acc[rubroNombre]) {
            acc[rubroNombre] += 1;
          } else {
            acc[rubroNombre] = 1;
          }
          return acc;
        }, {});

      // Convertir el objeto en un array para el gráfico
      const dataFormateada = Object.keys(productosPorRubro).map((rubro) => ({
        rubro: rubro,
        total_productos: productosPorRubro[rubro],
      }));
      console.log(dataFormateada);

      setProductosData(dataFormateada);
    } catch (error) {
      console.error('Error al obtener los datos de productos:', error);
    }
  };

  // Función para obtener exportaciones y calcular el total acumulado de FOB por año
  const fetchExportaciones = async () => {
    try {
      const response = await axios.get('http://localhost:8000/exportaciones/api/exportaciones/');
      const exportaciones = response.data;

      const fobPorAnio = exportaciones.reduce((acc, exportacion) => {
        const anio = exportacion.año;
        const fob = parseFloat(exportacion.fob_dolar);
        if (acc[anio]) {
          acc[anio] += fob;
        } else {
          acc[anio] = fob;
        }
        return acc;
      }, {});

      const dataFormateada = Object.keys(fobPorAnio).map((anio) => ({
        año: anio,
        total_fob: fobPorAnio[anio],
      }));

      setFobData(dataFormateada);
    } catch (error) {
      console.error('Error al obtener los datos de exportaciones:', error);
    }
  };

  // Llama a ambas APIs al montar el componente
  useEffect(() => {
    console.log('Componente fetch cargado');
    fetchProductos();
    fetchExportaciones();
  }, [selectedYear]);

  return (
    <div className="container mx-auto">
  <h2 className="text-center font-bold text-xl mb-4">Dashboard de Exportaciones</h2>
  
  {/* Filtro de Año */}
  <div className="mb-4">
        <label htmlFor="year-select" className="block text-center font-bold mb-2">Selecciona el Año:</label>
        <select
          id="year-select"
          value={selectedYear || ''}
          onChange={(e) => setSelectedYear(Number(e.target.value))}
          className="block mx-auto p-2 border rounded"
        >
          
          <option value={2023}>2023</option>
          <option value={2024}>2024</option>
        </select>
      </div>

  {/* Configura la grid con una sola columna en todas las pantallas */}
  <div className="grid grid-cols-1 gap-4">
    
    {/* Gráfico de áreas: Productos por rubro */}
    <div>
      <h3 className="text-center">Cantidad de productos por Rubro</h3>
      <ResponsiveContainer width="90%" height={500}>
        <BarChart data={productosData}>
          <CartesianGrid strokeDasharray="4 1" />
          <XAxis
            dataKey="rubro"
            interval={0}   // Muestra todas las etiquetas del eje X
            angle={-25}    // Rota las etiquetas si son largas
            textAnchor="end"  // Alinea las etiquetas
            tick={{ fontSize: 10 }}  // Reduce el tamaño de la fuente de las etiquetas
          />
          <YAxis />
          <Tooltip content={<CustomTooltipRubro />} />
          <Legend />
          <Bar  dataKey="total_productos" name="Total productos por Rubro" stroke="#3259B5" fill="#C0217E" />
        </BarChart>
      </ResponsiveContainer>
    </div>

    {/* Gráfico de barras: Acumulado de FOB Dólar por año */}
    {/* <div>
      <h3 className="text-center">Total FOB Dólar por Año</h3>
      <ResponsiveContainer width="90%" height={500}>
        <AreaChart data={fobData}>
          <CartesianGrid strokeDasharray="4 1" />
          <XAxis dataKey="año" />
          <YAxis 
            tickFormatter={(value) => {
              const numericValue = Number(value);
              return new Intl.NumberFormat('es-ES', {
                style: 'currency',
                currency: 'USD',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
              }).format(numericValue);
            }} 
          />
          <Tooltip content={<CustomTooltipFob />} />
          <Legend />
          <Area type='step' dataKey="total_fob" fill="#8884d8" />
        </AreaChart>
      </ResponsiveContainer>
    </div> */}
    
  </div>
</div>

  );
};
