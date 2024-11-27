#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const data = JSON.parse(body);
    const films = data.results;
    const count = films.filter(film =>
      film.characters.some(character => character.includes('/18/'))
    ).length;
    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
