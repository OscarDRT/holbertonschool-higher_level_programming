#!/usr/bin/node

const myVar = parseInt(process.argv[2], 10);

if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < myVar; row++) {
    console.log('X'.repeat(myVar));
  }
}
