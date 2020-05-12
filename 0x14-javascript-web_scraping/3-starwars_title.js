#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(url, function (error, response, body) {
  if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
