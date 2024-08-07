$(document).ready(() => {
    // Attach a click event handler to the DIV#red_header
    $('#red_header').click(() => {
        // Use jQuery to select the header element and change its color
        $('header').css('color', '#FF0000');
    });
});
