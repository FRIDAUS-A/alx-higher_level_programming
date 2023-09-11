#!/usr/bin/node

const len = process.argv.length;
const myArray = process.argv;
const newArray = [];
if (len === 2 || len === 3) {
  console.log('0');
} else {
  for (let index = 2; index < len; index++) {
    newArray.push(Number((myArray[index])));
    newArray.sort();
  }
  let pos = newArray.length - 1;
  while (newArray[pos] === newArray[pos - 1]) {
    pos -= 1;
  }
  console.log(newArray[pos - 1]);
}
