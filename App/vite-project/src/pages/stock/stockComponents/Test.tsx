import { useState, useEffect } from 'react';
import { Table } from '@mui/material';

function BasicTable({ parameter }) {
    const [data, setData] = useState(null);
    
    useEffect(() => {
        if (!data) { // Effettua la richiesta solo se i dati non sono stati già caricati
            fetch('http://localhost:5010/stock')
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    setData(data);
                })
                .catch(error => console.error('Errore:', error));
        }
    }, [data]); // Aggiungi data come dipendenza affinché l'effetto venga eseguito solo se i dati non sono stati già caricati

    return (
        <Table>
            <thead>
                <tr>
                    <th>Symbol</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Change</th>
                    <th>Change %</th>
                </tr>
            </thead>
            <tbody>
                {data && data[parameter] && data[parameter].map(item => (
                    <tr key={item.symbol}>
                        <td>{item.symbol}</td>
                        <td>{item.name}</td>
                        <td>{item.price}</td>
                        <td>{item.change}</td>
                        <td>{item.changePercent}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
}

export default BasicTable;
