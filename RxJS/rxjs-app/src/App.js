import React from 'react';
import './App.css';
import Title from './components/Title';
import Status from './components/Status';

function App() {
  return (
    <div className="App">
      <Title />
      <Status />
      <label>Red Count: </label>
      <p/>
      <label>Blue Count: </label>
    </div>
  );
}

export default App;
