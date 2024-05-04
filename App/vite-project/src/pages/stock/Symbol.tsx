// Codice del componente TabsSegmentedControls

import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import CandlestickChart from './stockComponents/CandleChart';

export default function TabsSegmentedControls() {
  const [data, setData] = useState(null);
  const [info, setInfo] = useState(null); // Aggiungi stato per le informazioni aggiuntive
  const { symbol } = useParams(); // Ottieni il parametro 'symbol' dall'URL
  useEffect(() => {
    if (!data) {
      // Effettua la richiesta solo se i dati non sono stati già caricati
      fetch(`http://localhost:5010/stock/${symbol}`)
        .then(response => response.json())
        .then(data => {
          setData(data.data); // Imposta solo i dati dalla risposta
          setInfo(data.info); // Imposta le informazioni aggiuntive dalla risposta
        })
        .catch(error => console.error('Errore:', error));
    }
  }, [data, symbol]); // Aggiungi symbol come dipendenza affinché l'effetto venga eseguito ogni volta che il symbol cambia

  return (
    <div>
      <h1>{symbol}</h1>
      {data && <CandlestickChart data={data} />} 
      {info && (
        <div>
          <h2>Informazioni aggiuntive</h2>
          <p>Nome: {info.name}</p>
          <p>Paese: {info.country}</p>
          <p>Valuta: {info.currency}</p>
          <img src={info.logo} alt="Logo" />
          {/* Aggiungi altri dettagli di info qui */}
        </div>
      )}
    </div>
  );
}
