import { createClient, print } from 'redis';
import { promisify } from 'util';

const clientInstance = createClient();

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

clientInstance.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

/**
 * Sets a new school in Redis.
 * @param {string} schoolName - The name of the school.
 * @param {string} value - The value to set for the school.
 */
function setNewSchool(schoolName, value) {
  clientInstance.set(schoolName, value, print);
}

/**
 * Displays the value of a school from Redis.
 * @param {string} schoolName - The name of the school to display.
 */
async function displaySchoolValue(schoolName) {
  // promisify the get method
  const getAsync = promisify(clientInstance.get).bind(clientInstance);
  const value = await getAsync(schoolName);
  console.log(value);
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
