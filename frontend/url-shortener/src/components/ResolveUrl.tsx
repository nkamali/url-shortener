import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

function ResolveUrl() {
  const [shortUrl, setShortUrl] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    
    // You can make the GET request here using fetch or axios
    // The response will be the long URL which can then be displayed

    const response = await fetch(`/api/v1/urls/${shortUrl}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    
    const data = await response.json();

    // use this data to display in some component
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Label>Enter short URL to resolve</Form.Label>
        <Form.Control type="text" placeholder="Enter short URL" value={shortUrl} onChange={e => setShortUrl(e.target.value)} required />
      </Form.Group>
      <Button variant="primary" type="submit">Resolve</Button>
    </Form>
  );
}

export default ResolveUrl;
