#!/usr/bin/node

const request = require('request');

// Check for correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie details
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error('Error: Unable to fetch movie data. Check Movie ID.');
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch and print each character's name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error('Error:', charErr);
        return;
      }
      if (charRes.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      }
    });
  });
});
