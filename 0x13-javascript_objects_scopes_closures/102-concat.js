#!/usr/bin/node
const fs = require('fs');
fs.readFile('fileA', (err, data1) => {
  if (err) throw err;
  process.stdout.write(data1.toString());
});
fs.readFile('fileB', (err, data2) => {
  if (err) throw err;
  process.stdout.write(data2.toString());
});
