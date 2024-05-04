import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Login from './pages/authentication/Login';
import Signup from './pages/authentication/Signup';
import Forgot from './pages/authentication/ForgotPassword';
import Home from './pages/main/Home';
import Data from './pages/main/Data';
import Stock from './pages/stock/Stock';
import Symbol from './pages/stock/Symbol';
import './App.css';

const theme = createTheme();

function App() {
  const renderRoutes = () => {
    return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/forgot" element={<Forgot />} />
        <Route path="/data" element={<Data />} />
        <Route path="/stock" element={<Stock />} />
        <Route path="/stock/:symbol" element={<Symbol />} />
      </Routes>
    );
  };

  return (
    <ThemeProvider theme={theme}>
      <Router>
        {renderRoutes()}
      </Router>
    </ThemeProvider>
  );
}

export default App;
