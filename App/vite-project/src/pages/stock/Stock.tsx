import Tabs from '@mui/joy/Tabs';
import TabList from '@mui/joy/TabList';
import Tab, { tabClasses } from '@mui/joy/Tab';
import { useState, useEffect } from 'react';
import TabPanel from '@mui/joy/TabPanel';
import StockTable from './stockComponents/StockTable';

export default function TabsSegmentedControls() {
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
    <Tabs aria-label="tabs" defaultValue={0} sx={{ bgcolor: 'transparent' }}>
      <TabList
        disableUnderline
        sx={{
          p: 0.5,
          gap: 0.5,
          borderRadius: 'xl',
          bgcolor: 'background.level1',
          [`& .${tabClasses.root}[aria-selected="true"]`]: {
            boxShadow: 'sm',
            bgcolor: 'background.surface',
          },
        }}
      >

        <Tab disableIndicator sx={{ flex: 1 }}>Best gainers</Tab>
        <Tab disableIndicator sx={{ flex: 1 }}>Most losers</Tab>
        <Tab disableIndicator sx={{ flex: 1 }}>Highest volume</Tab>
        <Tab disableIndicator sx={{ flex: 1 }}>Biggest USA</Tab>
      </TabList>
        <TabPanel value={0}>
          <StockTable data={data} type="gainers" />
        </TabPanel>
        <TabPanel value = {1}>
          <StockTable data={data} type="losers" />
        </TabPanel>
        <TabPanel value = {2}>
          <StockTable data={data} type="most_active" />
   
        </TabPanel>
        <TabPanel value = {3}>
  
        </TabPanel>

    </Tabs>


  );
}