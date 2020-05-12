#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, function (error, response, body) {
  fs.writeFile(path, body, (err) => {
    if (err) { console.log(err); }
  });
});