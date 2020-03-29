import React from 'react';
// import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import routes from app;

function App() {
  // const [user, setUser] = useState(0);

  // useEffect(() => {
  //   fetch('/').then(res => res.json()).then(data => {
  //     setUser(routes.;
  //   });
  // }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <title>{{ title }} - Microblog</title>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {/* <p>The current time is {currentTime}.</p> */}
      </header>
      <body>
        <h1>Hello, { user.username }!</h1>
      </body>
    </div>
  );
}

export default App;
