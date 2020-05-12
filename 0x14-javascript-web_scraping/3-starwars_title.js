#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

request.get(url, function (error, response, body) {
  if (response.statusCode === 404) { console.log(body); } else { console.log(JSON.parse(body).title); }
});
