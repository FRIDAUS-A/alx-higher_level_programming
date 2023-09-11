#!/usr/bin/node

const len = process.argv.length;
const myArray = process.argv;
const newArray = [];
if (len === 2 || len === 3) {
  console.log('%d', 0);
} else {
  for (let index = 2; index < len; index++) {
    newArray.push(Number((myArray[index])));
    newArray.sort();
  }
  console.log(newArray[newArray.length - 2]);
}
