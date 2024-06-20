#!/usr/bin/node
/* checks if the arg is num or not */
const arg = Number(process.argv[2]);
if (isNaN(arg)) { console.log('Not a number'); } else { console.log('My number: ' + process.argv[2]); }
