import React, { useEffect, useState } from 'react';
import './App.css';
import { PracticeRecords } from './components/PracticeRecords';

function App() {

  const [practiceRecords, setPracticeRecords] = useState([]);

  useEffect(() => {
    fetch('/practicerecords').then(response => response.json()).then(data => {
      console.log(data);
      setPracticeRecords(data.practiceRecords);
    });
  }, []);


  console.log(practiceRecords)
  
  return (
    <div className="App">
      
    <PracticeRecords PracticeRecordsArg={practiceRecords}/>
    </div>
  );
}

export default App;
