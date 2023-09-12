#!/usr/bin/node
const Square0 = require('./5-square');
module.exports = class Square extends Square0 {
  constructor (size) {
  super(size);
  this.size = size;
  }
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let indexY = 0; indexY < this.size; indexY++) {
        for (let indexX = 0; indexX < this.size; indexX++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
};
