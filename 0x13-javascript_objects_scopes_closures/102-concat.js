#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], (err, data1) => {
  if (err) throw err;
  fs.writeFile(process.argv[4], data1, (err) => {
    if (err) throw err;
  });
});
fs.readFile(process.argv[3], (err, data2) => {
  if (err) throw err;
  fs.appendFile(process.argv[4], data2, (err) => {
    if (err) throw err;
  });
});
