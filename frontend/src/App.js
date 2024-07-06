import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [trustScore, setTrustScore] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:8000/get-trust-score', { input });
    setTrustScore(response.data.trustScore);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
        <button type="submit">Get Trust Score</button>
      </form>
      {trustScore && <div>Trust Score: {trustScore}</div>}
    </div>
  );
}

export default App;
