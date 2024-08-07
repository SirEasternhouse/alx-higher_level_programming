$(document).ready(() => {
    // Define the API URL
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Fetch data from the API
    $.getJSON(apiUrl, (data) => {
        // Extract the translation of "hello"
        const helloTranslation = data.hello;

        // Display the translation in the DIV#hello
        $('#hello').text(helloTranslation);
    }).fail(() => {
        // Handle errors if the request fails
        $('#hello').text('Failed to load translation.');
    });
});
