#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // The file path is passed as an argument

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.trim()); // Ensures no trailing newlines or spaces
});
