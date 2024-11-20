#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  console.log(add(arg1, arg2));
}
