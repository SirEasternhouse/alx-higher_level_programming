$(document).ready(() => {
    // Attach a click event handler to the DIV#red_header
    $('#red_header').click(() => {
        // Add the class 'red' to the header element
        $('header').addClass('red');
    });
});
