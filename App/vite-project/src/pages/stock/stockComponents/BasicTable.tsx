import { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

function BasicTable({ allData, dataType }) {
    const [filteredData, setFilteredData] = useState(null);

    useEffect(() => {
        if (allData && dataType) {
            // Filtra i dati in base al tipo di dati richiesto
            switch (dataType) {
                case 'gainers':
                    setFilteredData(allData.gainers);
                    break;
                case 'losers':
                    setFilteredData(allData.losers);
                    break;
                case 'volume':
                    setFilteredData(allData.volume);
                    break;
                case 'usa':
                    setFilteredData(allData.usa);
                    break;
                default:
                    setFilteredData(null);
            }
        }
    }, [allData, dataType]);

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
                {filteredData && filteredData.map((stock, index) => (
                    <TableRow key={index}>
                        <TableCell>{stock.symbol}</TableCell>
                        <TableCell>{stock.name}</TableCell>
                        <TableCell>{stock.price}</TableCell>
                        <TableCell>{stock.change}</TableCell>
                        <TableCell>{stock.changePercent}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    );
}

export default BasicTable;
