#!/usr/bin/node

const fs = require('fs');

// Get arguments from the command line
const filePath = process.argv[2];
const content = process.argv[3];

// Write content to the file
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
