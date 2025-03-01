import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Secure Axios instance with global settings
const secureAxios = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Base API URL
  timeout: 5000, // 5 seconds timeout
  withCredentials: true, // Ensures cookies & authentication are sent
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${localStorage.getItem('access_token') || ''}`, // Secure token handling
  },
});

function Home() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    secureAxios
      .get('/api/products')
      .then((response) => {
        console.log('📌 API Response:', response.data); // Debugging Log
        setProducts(response.data);
      })
      .catch((err) => {
        // ✅ 변수명 충돌 방지
        console.error('❌ Error fetching data:', err);
        if (err.response) {
          setError(`Server Error: ${err.response.status} - ${err.response.data.message || 'Unknown error'}`);
        } else if (err.request) {
          setError('Network Error: No response received from the server.');
        } else {
          setError(`Request Error: ${err.message}`);
        }
      });
  }, []);

  return (
    <div className="grid grid-cols-3 gap-4 p-10">
      {products.map((product) => (
        <div key={product.id} className="border p-4 rounded-lg shadow-md">
          <img src={product.image_url} alt={product.name} className="w-full h-40 object-cover rounded-md" />
          <h2 className="text-lg font-bold mt-2">{product.name}</h2>
          <p className="text-gray-500">
            $
            {product.price}
          </p>
        </div>
      ))}
    </div>
  );
}
export default Home;
