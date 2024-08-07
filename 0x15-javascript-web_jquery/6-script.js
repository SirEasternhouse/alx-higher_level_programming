$(document).ready(() => {
    // Attach a click event handler to the DIV#update_header
    $('#update_header').click(() => {
        // Update the text of the <header> element
        $('header').text('New Header!!!');
    });
});
