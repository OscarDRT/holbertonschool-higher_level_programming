#!/usr/bin/node

const myVar = parseInt(process.argv[2], 10);

if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < myVar; index++) {
    console.log('C is fun');
  }
}
