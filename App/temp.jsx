import { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';

function BasicTable() {
    const [stockData, setStockData] = useState([]);

    useEffect(() => {  
        fetch('http://localhost:5010/stock')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setStockData(data);
            })
            .catch(error => console.error('Errore:', error));
    }, []);

    return (
        <Table>
            <TableHead>
                <TableRow>
                    <TableCell>Symbol</TableCell>
                    <TableCell>Name</TableCell>
                    <TableCell>Price</TableCell>
                    <TableCell>Change</TableCell>
                    <TableCell>Change %</TableCell>
                </TableRow>
            </TableHead>
            <TableBody>
                {stockData.map((stockCategory, categoryIndex) => (
                    <React.Fragment key={categoryIndex}>
                        <TableRow>
                            <TableCell colSpan={5} style={{ fontWeight: 'bold' }}>
                                {stockCategory.category}
                            </TableCell>
                        </TableRow>
                        {stockCategory.stocks.map((stock, index) => (
                            <TableRow key={index}>
                                <TableCell>{stock.symbol}</TableCell>
                                <TableCell>{stock.name}</TableCell>
                                <TableCell>{stock.price}</TableCell>
                                <TableCell>{stock.change}</TableCell>
                                <TableCell>{stock.changePercent}</TableCell>
                            </TableRow>
                        ))}
                    </React.Fragment>
                ))}
            </TableBody>
        </Table>
    );
}

export default BasicTable;
