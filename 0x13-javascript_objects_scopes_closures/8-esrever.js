#!/usr/bin/node
exports.esrever = function (list) {
  let index = list.length - 1;
  newList = []
  while (index >= 0) {
    newList.push(list[index]);
    index--;
  }
  return (newList);
}
