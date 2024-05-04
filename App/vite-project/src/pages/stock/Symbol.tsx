import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import CandlestickChart from './stockComponents/CandleChart';

export default function TabsSegmentedControls() {
  const [data, setData] = useState(null);
  const { symbol } = useParams(); // Ottieni il parametro 'symbol' dall'URL
  useEffect(() => {
    if (!data) {
      // Effettua la richiesta solo se i dati non sono stati già caricati
      fetch(`http://localhost:5010/stock/${symbol}`)
        .then(response => response.json())
        .then(data => {
          setData(data);
        })
        .catch(error => console.error('Errore:', error));
    }
  }, [data, symbol]); // Aggiungi symbol come dipendenza affinché l'effetto venga eseguito ogni volta che il symbol cambia

  return (
    <div>
      <h1>{symbol}</h1>
      <CandlestickChart data={data} ></CandlestickChart>
    </div>

  );
}
