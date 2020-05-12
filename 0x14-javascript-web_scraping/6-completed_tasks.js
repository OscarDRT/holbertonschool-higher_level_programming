#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  const obj = {};
  if (err) { console.log(err); } else {
    const todos = JSON.parse(body);
    todos.forEach(element => {
      if (element.completed) {
        if (!(obj[element.userId])) {
          obj[element.userId] = 1;
        } else {
          obj[element.userId] += 1;
        }
      }
    });
  }
  console.log(obj);
});
