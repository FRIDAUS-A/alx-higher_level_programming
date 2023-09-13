#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
let set = new Set(Object.values(dict));
set = [...set];
const Entries = Object.entries(dict);
for (let count = 0; count < set.length; count++) {
  const tmpList = [];
  for (let index = 0; index < Entries.length; index++) {
    if (set[count] === Entries[index][1]) {
      tmpList.push(Entries[index][0]);
    }
  }
  newDict[set[count]] = tmpList;
}
console.log(newDict);
