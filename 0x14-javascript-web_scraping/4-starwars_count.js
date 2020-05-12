#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  let count = 0;
  let obj = JSON.parse(body);
  obj = obj.results;
  obj.forEach(element => {
    const character = element.characters;
    if (character.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
