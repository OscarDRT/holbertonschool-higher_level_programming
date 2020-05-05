#!/usr/bin/node

const array = process.argv.slice(2);

if (array.length <= 1) {
  console.log('0');
} else {
  for (let index = 0; index < array.length; index++) {
    array[index] = parseInt(array[index], 10);
  }
  array.sort(function (a, b) {
    return a - b;
  });

  array.pop();
  const len = array.length - 1;
  console.log(array[len]);
}
