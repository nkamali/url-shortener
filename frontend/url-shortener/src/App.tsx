import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import UrlInput from './components/UrlInput';
import ResolveUrl from './components/ResolveUrl';

function App() {
  return (
    <div className="App">
      <h1>URL Shortener</h1>
      <UrlInput />
      <ResolveUrl />
    </div>
  );
}

export default App;
