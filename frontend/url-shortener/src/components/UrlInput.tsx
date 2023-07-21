import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

function UrlInput() {
  const [url, setUrl] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    
    // You can make the POST request here using fetch or axios
    // The response will be the shortened URL which can then be displayed using the UrlDisplay component

    const response = await fetch('/api/v1/urls/shorten/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url
      }),
    });
    
    const data = await response.json();

    // use this data to display in UrlDisplay component
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Label>Enter URL to shorten</Form.Label>
        <Form.Control type="text" placeholder="Enter URL" value={url} onChange={e => setUrl(e.target.value)} required />
      </Form.Group>
      <Button variant="primary" type="submit">Shorten</Button>
    </Form>
  );
}

export default UrlInput;
