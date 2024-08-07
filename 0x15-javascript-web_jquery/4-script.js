$(document).ready(() => {
    // Attach a click event handler to the DIV#toggle_header
    $('#toggle_header').click(() => {
        const header = $('header');
        
        // Check the current class and toggle between red and green
        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else {
            header.removeClass('green').addClass('red');
        }
    });
});
