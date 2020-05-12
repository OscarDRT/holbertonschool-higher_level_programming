#!/usr/bin/node

const path = process.argv.slice(2);
const fs = require('fs');

fs.readFile(path[0], { encoding: 'utf8' }, (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
