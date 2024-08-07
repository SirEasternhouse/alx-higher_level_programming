$(document).ready(() => {
    // Define the API URL
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Fetch data from the API
    $.getJSON(apiUrl, (data) => {
        // Get the list of movies
        const movies = data.results;
        
        // Clear the list before adding new items
        $('#list_movies').empty();

        // Iterate over the movies and append each title to the list
        movies.forEach((movie) => {
            const listItem = $('<li></li>').text(movie.title);
            $('#list_movies').append(listItem);
        });
    }).fail(() => {
        // Handle errors if the request fails
        $('#list_movies').text('Failed to load movie titles.');
    });
});
