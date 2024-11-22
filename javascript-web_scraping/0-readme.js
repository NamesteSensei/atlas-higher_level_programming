#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Error: Missing file path argument.');
  process.exit(1); // Exit with an error code
}

// Read the file content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print error if reading fails
  } else {
    console.log(data); // Print file content
  }
});
