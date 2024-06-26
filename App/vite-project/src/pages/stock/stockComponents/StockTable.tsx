import React, { useState } from 'react';
import Table from '@mui/joy/Table';
import Sheet from '@mui/joy/Sheet';
import { ArrowUpward, ArrowDownward } from '@mui/icons-material';
import Chip from '@mui/joy/Chip';
import KeyboardArrowLeftIcon from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';

function StockTable({ data, type }) {
  const [sortBy, setSortBy] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');
  const [currentPage, setCurrentPage] = useState(1);

  const rowsPerPage = 20;

  const handleSort = (column) => {
    if (sortBy === column) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(column);
      setSortDirection('asc');
    }
  };

  const sortedData = data && data[type] && [...data[type]].sort((a, b) => {
    if (sortBy) {
      if (a[sortBy] < b[sortBy]) {
        return sortDirection === 'asc' ? -1 : 1;
      }
      if (a[sortBy] > b[sortBy]) {
        return sortDirection === 'asc' ? 1 : -1;
      }
    }
    return 0;
  });

  const totalPages = 5;
  const startIndex = (currentPage - 1) * rowsPerPage;
  const endIndex = startIndex + rowsPerPage;

  const getSortIcon = (column) => {
    if (sortBy === column) {
      return sortDirection === 'asc' ? <ArrowUpward /> : <ArrowDownward />;
    }
    return null;
  };

  const getChipColor = (value) => {
    if (value > 0) {
      return "success"; // Verde se il valore è maggiore di zero
    } else if (value < 0) {
      return "danger"; // Rosso se il valore è minore di zero
    } else {
      return "neutral"; // Grigio se il valore è zero o altro
    }
  };

  const goToPreviousPage = () => {
    setCurrentPage(prevPage => Math.max(1, prevPage - 1));
  };

  const goToNextPage = () => {
    setCurrentPage(prevPage => Math.min(totalPages, prevPage + 1));
  };


  return (
    <Sheet variant="soft" sx={{ pt: 1, borderRadius: 5 }}>
      <Table
        stripe="odd"
        hoverRow
        sx={{ captionSide: 'top', '& tbody': { bgcolor: 'background.surface' } }}
      >
        <thead>
          <tr>
            <th
              style={{ cursor: 'pointer', width: '2%', textAlign: 'center', verticalAlign: 'middle' }}>#
            </th>
            <th
              onClick={() => handleSort('symbol')}
              style={{ cursor: 'pointer', width: '6.5%', textAlign: 'center', verticalAlign: 'middle' }}
            >
              {getSortIcon('symbol')} Symbol
            </th>
            <th
              onClick={() => handleSort('name')}
              style={{ cursor: 'pointer', width: '21.5%', textAlign: 'center', verticalAlign: 'middle' }}
            >
              {getSortIcon('name')} Name
            </th>
            <th
              onClick={() => handleSort('price')}
              style={{ cursor: 'pointer', width: '10%', textAlign: 'center', verticalAlign: 'middle' }}
            >
              {getSortIcon('price')} Price ($)
            </th>
            <th
              onClick={() => handleSort('change')}
              style={{ cursor: 'pointer', width: '10%', textAlign: 'center', verticalAlign: 'middle' }}
            >
              {getSortIcon('change')} Change ($)
            </th>
            <th
              onClick={() => handleSort('changesPercentage')}
              style={{ cursor: 'pointer', width: '10%', textAlign: 'center', verticalAlign: 'middle' }}
            >
              {getSortIcon('changesPercentage')} Change (%)
            </th>
            <th style={{ width: '10%', textAlign: 'center', verticalAlign: 'middle' }}>Volume</th>
            <th style={{ width: '10%', textAlign: 'center', verticalAlign: 'middle' }}>Market Cap</th>
            <th style={{ width: '7%', textAlign: 'center', verticalAlign: 'middle' }}>P/E Ratio</th>
          </tr>
        </thead>
        <tbody>
          {sortedData && sortedData.slice(startIndex, endIndex).map((item, index) => (
            <tr key={item.symbol}>
              <td style={{ textAlign: 'center', verticalAlign: 'middle', opacity: '0.8' }}>{startIndex + index + 1}</td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle', cursor: 'pointer' }}>
                <a href={`stock/${item.symbol}`}><u>{item.symbol}</u></a>
              </td>
              <td style={{ textAlign: 'left', verticalAlign: 'middle' }}>{item.name}</td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}><b>{item.price} $</b></td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}>
                <Chip
                  color={getChipColor(item.change)}
                  size="lg"
                  variant="solid"
                  label={`${item.change} %`}
                >
                  {item.change} $
                </Chip>
              </td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}>
                <Chip
                  color={getChipColor(item.percent_change)}
                  size="lg"
                  variant="solid"
                  label={`${item.percent_change} %`}
                >
                  {item.percent_change} %
                </Chip>
              </td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}>{item.volume}</td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}>{item.market_cap}</td>
              <td style={{ textAlign: 'center', verticalAlign: 'middle' }}>{item.pe_ratio}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      <div style={{ textAlign: 'center', marginTop: '1rem' }}>
        <button onClick={goToPreviousPage} disabled={currentPage === 1}>
          <KeyboardArrowLeftIcon />
        </button>
        <span style={{ margin: '0 0.5rem', verticalAlign: 'middle' }}>{currentPage} / {totalPages}</span>
        <button onClick={goToNextPage} disabled={currentPage === totalPages}>
          <KeyboardArrowRightIcon />
        </button>
      </div>
    </Sheet>
  );
}
export default StockTable;
