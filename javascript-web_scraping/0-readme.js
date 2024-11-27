#!/usr/bin/node

const fs = require('fs');
<<<<<<< HEAD
=======
const path = require('path');
const filePath = process.argv[2];
>>>>>>> b6f067812c92fff1adb9c829f4613b4087a3797c

const filePath = process.argv[2]; // The file path is passed as an argument

<<<<<<< HEAD
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
=======
// Normalize file path for cross-platform compatibility
const normalizedPath = path.resolve(filePath);

// Read the file content
fs.readFile(normalizedPath, 'utf-8', (err, data) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error('Error: File not found.');
    } else if (err.code === 'EACCES') {
      console.error('Error: Permission denied.');
    } else {
      console.error('Error:', err.message);
    }
    process.exit(1); // Exit with an error code
  } else {
    console.log(data); // Print file content
>>>>>>> b6f067812c92fff1adb9c829f4613b4087a3797c
  }
  console.log(data);
});
