#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) { console.log(error); } else {
    const movies = JSON.parse(body).results;
    let count = 0;

    movies.forEach(element => {
      const characters = element.characters;
      characters.forEach(character => {
        if (character.includes('18')) { count++; }
      });
    });
    console.log(count);
  }
});
