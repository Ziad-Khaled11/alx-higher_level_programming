#!/usr/bin/node
/* prints a square */
const arg = Number(process.argv[2]);
if (isNaN(arg)) { console.log('Missing size'); } else {
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
