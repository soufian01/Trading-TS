import React, { useEffect, useRef } from 'react';
import { createChart } from 'lightweight-charts';

export default function CandlestickChart({ data }) {
  const chartContainerRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (data && data.length > 0) {
      // Crea un nuovo grafico solo se non esiste già un'istanza
      if (!chartInstance.current) {
        chartInstance.current = createChart(chartContainerRef.current, {
          width: chartContainerRef.current.clientWidth,
          height: 400,
        });
      }

      const candlestickSeries = chartInstance.current.addCandlestickSeries();

      // Trasforma i dati in un formato accettabile per Lightweight Charts
      const chartData = data.map(item => ({
        time: item.Date / 1000, // Dividi per 1000 per ottenere millisecondi
        open: item.Open,
        high: item.High,
        low: item.Low,
        close: item.Close,
      }));

      // Aggiungi i dati al grafico
      candlestickSeries.setData(chartData);
    }
  }, [data]);

  return <div ref={chartContainerRef} style={{ height: '400px' }}></div>;
}
