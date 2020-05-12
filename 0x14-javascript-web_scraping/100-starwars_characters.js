#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

request.get(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    const character = JSON.parse(body).characters;
    character.forEach(element => {
      request.get(element, (err, response, body) => {
        if (error) { console.log(error); } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
