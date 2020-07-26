import React, { useEffect, useState } from 'react';
import './App.css';
import Home from './components/Home';
import Logs from './components/Logs';
import Calendar from './components/Calendar';
import Profile from './components/Profile';

export default class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      page: 'home',
    }
  }

  setToPage(page) {
    this.setState({
      page: page,
    })
  }

  
  render() {
    const pageState = this.state.page;
    let pageContent;
    if (pageState == 'home') {
      pageContent = <Home />
    } else if (pageState == 'logs') {
      pageContent = <Logs />
    } else if (pageState == 'calendar') {
      pageContent = <Calendar />
    } else if (pageState == 'profile') {
      pageContent = <Profile />
    } 
    

    return (
      <div>
        <div className="container">
          <div className="header-navbar">
            <nav class="navbar navbar-dark bg-dark">
              <span class="navbar-brand mb-0 h1">Navbar</span>
              <button class="btn" type="button">Search button</button>

            </nav>
              
          </div>

          <div>{pageContent}</div>

          <div className="footer-navbar">
            <nav class="navbar navbar-dark bg-dark">
              <button class="btn" type="button" onClick={() => this.setToPage('home')}>Home</button>
              <button class="btn" type="button" onClick={() => this.setToPage('logs')}>Practice Logs</button>
              <button class="btn" type="button" onClick={() => this.setToPage('calendar')}>Calendar</button>
              <button class="btn" type="button" onClick={() => this.setToPage('profile')}>Profile</button>
            </nav>
          </div>

        </div>  
      </div>
      
    );
  }
  
}

