#!/usr/bin/node

const fs = require('fs');
const path = require('path');
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Error: Missing file path argument.');
  process.exit(1); // Exit with an error code
}

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
  }
});
