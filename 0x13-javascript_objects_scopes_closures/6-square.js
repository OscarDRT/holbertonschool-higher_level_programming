#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
