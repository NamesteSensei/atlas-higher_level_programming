#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
console.log(args.length < 2 ? 0 : args[1]);
