#!/usr/bin/node

const Rectangle = require('./4-rectangle');
const Square = require('./6-square');

console.log('Task 4: Rectangle #4');
const r1 = new Rectangle(4, 2);
r1.print();
r1.double();
console.log('Doubled:');
r1.print();
r1.rotate();
console.log('Rotated:');
r1.print();

console.log('\nTask 5: Square #0');
const s1 = new Square(4);
s1.print();

console.log('\nTask 6: Square #1');
const s2 = new Square(4);
s2.charPrint();
s2.charPrint('C');
