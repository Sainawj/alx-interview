#!/usr/bin/node

// Import the 'request' module to handle HTTP requests
const request = require('request');

// Send a GET request to the API to fetch the film details based on the film ID passed as a command-line argument (process.argv[2])
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  // If an error occurs during the request, throw an error
  if (err) throw err;

  // Parse the response body to extract the 'characters' array, which contains URLs for the actors in the film
  const actors = JSON.parse(body).characters;

  // Call the function 'exactOrder' to process the list of actors in the exact order
  exactOrder(actors, 0);
});

// Define the 'exactOrder' function to recursively fetch and print actor names in the correct order
const exactOrder = (actors, x) => {
  // Base case: if we've processed all actors, exit the function
  if (x === actors.length) return;

  // Send a GET request to fetch the details of the actor using the URL at actors[x]
  request(actors[x], function (err, res, body) {
    // If an error occurs during the request, throw an error
    if (err) throw err;

    // Parse the response body to get the actor's name and print it to the console
    console.log(JSON.parse(body).name);

    // Recursively call 'exactOrder' with the next actor (x + 1)
    exactOrder(actors, x + 1);
  });
};