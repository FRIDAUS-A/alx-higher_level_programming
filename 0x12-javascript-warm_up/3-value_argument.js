#!/usr/bin/node

let count = 0;
const args = process.argv;
while (args[count]) {
  count++;
}
if (count >= 3) {
  console.log(args[2]);
} else if (count === 2) {
  console.log('No argument');
}
