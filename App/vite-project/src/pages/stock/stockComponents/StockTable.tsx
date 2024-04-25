import React, { useState } from 'react';
import Table from '@mui/joy/Table';
import Sheet from '@mui/joy/Sheet';
import { ArrowUpward, ArrowDownward, NavigateBefore, NavigateNext } from '@mui/icons-material';

function StockTable({ data, type }) {
  const [sortBy, setSortBy] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');
  const [currentPage, setCurrentPage] = useState(1);

  const rowsPerPage = 10;

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

  const totalPages = Math.ceil(sortedData.length / rowsPerPage);

  const startIndex = (currentPage - 1) * rowsPerPage;
  const endIndex = startIndex + rowsPerPage;

  const getSortIcon = (column) => {
    if (sortBy === column) {
      return sortDirection === 'asc' ? <ArrowUpward /> : <ArrowDownward />;
    }
    return null;
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
            style={{ cursor: 'pointer', width: '5%', textAlign: 'center' }}>#</th>
            <th
              onClick={() => handleSort('symbol')}
              style={{ cursor: 'pointer', width: '10%', textAlign: 'center' }}
            >
              {getSortIcon('symbol')} Symbol
            </th>
            <th
              onClick={() => handleSort('name')}
              style={{ cursor: 'pointer', width: '40%', textAlign: 'center' }}
            >
              {getSortIcon('name')} Name
            </th>
            <th
              onClick={() => handleSort('price')}
              style={{ cursor: 'pointer', textAlign: 'center' }}
            >
              {getSortIcon('price')} Price
            </th>
            <th
              onClick={() => handleSort('change')}
              style={{ cursor: 'pointer', textAlign: 'center' }}
            >
              {getSortIcon('change')} Change
            </th>
            <th
              onClick={() => handleSort('changesPercentage')}
              style={{ cursor: 'pointer', textAlign: 'center' }}
            >
              {getSortIcon('changesPercentage')} Change %
            </th>
          </tr>
        </thead>
        <tbody>
          {sortedData && sortedData.slice(startIndex, endIndex).map((item, index) => (
            <tr key={item.symbol}>
              <td style={{ textAlign: 'center', width:'10%'}}>{startIndex + index + 1}</td>
              <td style={{ textAlign: 'center', width:'30%' }}>{item.symbol}</td>
              <td style={{ textAlign: 'center' }}>{item.name}</td>
              <td style={{ textAlign: 'center' }}>{item.price} $</td>
              <td style={{ textAlign: 'center' }}>{item.change} %</td>
              <td style={{ textAlign: 'center' }}>{item.changesPercentage} %</td>
            </tr>
          ))}
        </tbody>
      </Table>
      <div style={{ textAlign: 'center', marginTop: '1rem' }}>
        <button onClick={goToPreviousPage} disabled={currentPage === 1}>
          <NavigateBefore />
        </button>
        <span style={{ margin: '0 0.5rem' }}>{currentPage} / {totalPages}</span>
        <button onClick={goToNextPage} disabled={currentPage === totalPages}>
          <NavigateNext />
        </button>
      </div>
    </Sheet>
  );
}

export default StockTable;
