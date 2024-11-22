#!/usr/bin/node

const nbOccurences = require('./7-occurrences').nbOccurences;
const esrever = require('./8-esrever').esrever;
const logMe = require('./9-logme').logMe;
const converter = require('./10-converter').converter;

console.log('Task 7: Occurrences');
console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3)); // 1
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3)); // 4
console.log(nbOccurences(['S', 12, 'c', 'S', 'School', 8], 'S')); // 2

console.log('\nTask 8: Esrever');
console.log(esrever([1, 2, 3, 4, 5])); // [5, 4, 3, 2, 1]
console.log(esrever(['School', 89, { id: 12 }, 'String'])); // ['String', { id: 12 }, 89, 'School']

console.log('\nTask 9: Log Me');
logMe('Hello'); // 0: Hello
logMe('Best'); // 1: Best
logMe('School'); // 2: School

console.log('\nTask 10: Number Conversion');
const base10To2 = converter(2);
console.log(base10To2(10)); // 1010
console.log(base10To2(15)); // 1111

const base10To16 = converter(16);
console.log(base10To16(10)); // a
console.log(base10To16(15)); // f
