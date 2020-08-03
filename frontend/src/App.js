import React from 'react';
import './App.css';
import Home from './components/Home';
import Logs from './components/Logs';
import Calendar from './components/Calendar';
import Profile from './components/Profile';
import { Route, Link } from "react-router-dom";

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
    return (
      <div>
        <div className="container">
          <div className="header-navbar">
            <nav className="navbar navbar-dark bg-dark">
              <span className="navbar-brand mb-0 h1">Navbar</span>
              <Link to="/search"><button className="btn" type="button">Search button</button></Link>

            </nav>
              
          </div>

          <Route exact path="/" component={Home}/>
          <Route exact path="/logs" component={Logs}/>
          <Route exact path="/calendar" component={Calendar}/>
          <Route exact path="/profile" component={Profile}/>



          <div className="footer-navbar">
            <nav className="navbar navbar-dark bg-dark">
              <Link to="/"><button className="btn" type="button" onClick={() => this.setToPage('home')}>Home</button></Link>
              <Link to="/logs"><button className="btn" type="button" onClick={() => this.setToPage('logs')}>Practice Logs</button></Link>
              <Link to="/calendar"><button className="btn" type="button" onClick={() => this.setToPage('calendar')}>Calendar</button></Link>
              <Link to="/profile"><button className="btn" type="button" onClick={() => this.setToPage('profile')}>Profile</button></Link>
            </nav>
          </div>

        </div>  
      </div>
      
    );
  }
  
}

