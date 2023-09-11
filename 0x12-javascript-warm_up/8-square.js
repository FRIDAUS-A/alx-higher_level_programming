#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
}
for (let index = 0; index < size; index++) {
  for (let Subindex = 0; Subindex < size; Subindex++) {
    process.stdout.write('X');
  }
  console.log();
}
