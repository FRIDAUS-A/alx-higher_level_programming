#!/usr/bin/node

const len = process.argv.length - 1;
if (len === 2) {
  console.log('Argument found');
} else if (len > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
