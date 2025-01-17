import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Optional: Add CSS for global styles
import App from './App'; // Import the main App component

const root = ReactDOM.createRoot(document.getElementById('root')); // Attach to the root div in index.html
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);