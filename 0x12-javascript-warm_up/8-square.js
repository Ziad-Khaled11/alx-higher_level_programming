#!/usr/bin/node
/* prints a square */
const arg = Number(process.argv[2]);
if (isNaN(arg)) { console.log('Missing size'); } else {
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log('X');
    }
    console.log();
  }
}
