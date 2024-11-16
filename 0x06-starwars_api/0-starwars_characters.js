#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the Movie ID
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Error: Unable to fetch movie data. Check Movie ID.');
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch character names concurrently
  Promise.all(
    characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charErr, charRes, charBody) => {
          if (charErr) {
            reject(charErr);
          } else if (charRes.statusCode !== 200) {
            reject(new Error('Failed to fetch character data'));
          } else {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          }
        });
      });
    })
  )
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((fetchError) => {
      console.error('Error fetching characters:', fetchError.message);
    });
});
