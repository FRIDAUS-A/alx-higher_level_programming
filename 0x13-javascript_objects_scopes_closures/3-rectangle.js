#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || w === undefined || h === undefined)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let indexY = 0; indexY < this.height; indexY++) {
      for (let indexX = 0; indexX < this.width; indexX++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
};
