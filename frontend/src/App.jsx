import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Scans from './pages/Scans';
import { isAuthenticated } from './services/api';

function App() {
  const [isAuth, setIsAuth] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      const auth = await isAuthenticated();
      setIsAuth(auth);
      setLoading(false);
    };
    checkAuth();
  }, []);

  const PrivateRoute = ({ children }) => {
    return isAuth ? children : <Navigate to="/login" />;
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login setIsAuth={setIsAuth} />} />
        <Route
          path="/"
          element={
            <PrivateRoute>
              <Home />
            </PrivateRoute>
          }
        />
        <Route
          path="/scans"
          element={
            <PrivateRoute>
              <Scans />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
