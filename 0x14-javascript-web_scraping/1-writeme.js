#!/usr/bin/node

const fs = require('fs');
let path = process.argv.slice(2);
const text = path[1];
path = path[0];

fs.writeFile(path, text, (err) => {
  if (err) { console.log(err); }
});
