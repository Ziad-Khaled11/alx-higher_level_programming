#!/usr/bin/node
/* adds two args numbers */

function add (a, b) {
  const arg = Number(a);
  const arg2 = Number(b);
  if (isNaN(arg) && isNaN(arg2)) { console.log(arg); } else {
    const num1 = Number(a);
    const num2 = Number(b);
    const sum = num1 + num2;
    console.log(sum);
  }
}

add(process.argv[2], process.argv[3]);
