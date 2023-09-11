#!/usr/bin/node

for (let index = 0; index < process.argv[2]; index++) {
  for (let Subindex = 0; Subindex < process.argv[2]; Subindex++) {
    process.stdout.write('X');
  }
  console.log();
}
