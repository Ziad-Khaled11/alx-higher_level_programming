#!/usr/bin/node
/* prints second max */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const arr = [-1000];
  for (let i = 0; i < args.length; i++) {
    arr.push(Number(args[i]));
  }
  const max = Math.max(...arr);
  const index = arr.indexOf(max);
  let Max = -1000;
  for (let i = 0; i < arr.length; i++) {
    if (i === index) {
      continue;
    } else {
      if (arr[i] > Max) {
        Max = arr[i];
      }
    }
  }
  console.log(Max);
}
