#!/usr/bin/node

const len = process.argv.length - 1;
if (len > 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
