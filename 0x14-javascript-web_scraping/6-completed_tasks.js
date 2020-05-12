#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) { console.log(err); } else {
    const todos = JSON.parse(body);
    const obj = {};
    todos.forEach(element => {
      obj[element.userId] = 0;
    });
    todos.forEach(element => {
      if (element.completed === true) {
        obj[element.userId] += 1;
      }
    });
  }
  console.log(obj);
});
