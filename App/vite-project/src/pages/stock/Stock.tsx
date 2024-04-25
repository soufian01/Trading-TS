import Tabs from '@mui/joy/Tabs';
import TabList from '@mui/joy/TabList';
import Tab, { tabClasses } from '@mui/joy/Tab';
import TabPanel from '@mui/joy/TabPanel';
import StockTable from './stockComponents/StockTable';
import Test from './stockComponents/Test';
//yerr
export default function TabsSegmentedControls() {

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
          <Test parameter="gainers"></Test>
        </TabPanel>
        <TabPanel value = {1}>
          <Test parameter="losers"></Test>
        </TabPanel>
        <TabPanel value = {2}>
          <Test parameter="actives"></Test>
        </TabPanel>
        <TabPanel value = {3}>
          <Test></Test>
        </TabPanel>

    </Tabs>


  );
}