#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film =>
      film.characters.some(characterUrl => characterUrl.endsWith(`/${wedgeAntillesId}/`))
    ).length;
    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
