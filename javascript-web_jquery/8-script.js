#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach((film) => {
    $('#list_movies').append(`<li>${film.title}</li>`);
  });
});
