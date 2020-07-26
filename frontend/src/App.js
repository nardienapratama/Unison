import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
 
  return (
    <div className="container">
      <div className="header-navbar">
        <nav class="navbar navbar-dark bg-dark">
          <span class="navbar-brand mb-0 h1">Navbar</span>
        </nav>
          
      </div>

      <div className="footer-navbar">
        <nav class="navbar navbar-dark bg-dark">
          <a class="navbar-brand" href="#">Fixed bottom</a>
        </nav>
      </div>

    </div>
    
  );
}

export default App;
