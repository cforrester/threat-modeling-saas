import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ThreatModels from './ThreatModels'; // Example component
import Home from './Home'; // Another page

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/threat-models" element={<ThreatModels />} />
      </Routes>
    </Router>
  );
}

export default App;
