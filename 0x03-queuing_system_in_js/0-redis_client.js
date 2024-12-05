import { createClient } from 'redis';

const clientInstance = createClient();

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

clientInstance.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});
