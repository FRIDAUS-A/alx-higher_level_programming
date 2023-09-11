#!/usr/bin/node

function factorial (n) {
  n = Number(n);
  if (n === 0 || isNaN(n) || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(process.argv[2]));
