$(document).ready(() => {
    // Define the API URL
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    // Fetch data from the API
    $.getJSON(apiUrl, (data) => {
        // Extract the character name
        const characterName = data.name;

        // Display the character name in the DIV#character
        $('#character').text(characterName);
    }).fail(() => {
        // Handle errors if the request fails
        $('#character').text('Failed to load character name.');
    });
});
