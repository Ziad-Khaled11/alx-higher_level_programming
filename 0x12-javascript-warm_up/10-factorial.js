#!/usr/bin/node
/* calculate the factorial */

function factorial (arg) {
  if (arg === 0 || isNaN(arg)) {
    return (1);
  } else if (arg < 0) {
    return (-1);
  } else {
    return (arg * factorial(arg - 1));
  }
}

factorial(Number(process.argv[2]));
