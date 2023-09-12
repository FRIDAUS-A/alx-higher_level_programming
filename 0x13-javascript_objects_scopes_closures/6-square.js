#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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
