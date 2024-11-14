#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];

  // Fetch the film details by ID
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }

    try {
      const charactersURL = JSON.parse(body).characters;

      // Fetch all character names using Promises
      const characterPromises = charactersURL.map(url =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, characterBody) => {
            if (promiseErr) {
              reject(promiseErr);
            } else {
              resolve(JSON.parse(characterBody).name);
            }
          });
        })
      );

      // Resolve all promises and print the character names
      Promise.all(characterPromises)
        .then(names => console.log(names.join('\n')))
        .catch(promiseErr => console.error('Error fetching character names:', promiseErr));
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
}
