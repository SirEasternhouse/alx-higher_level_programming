$(document).ready(() => {
    // Attach a click event handler to the DIV#add_item
    $('#add_item').click(() => {
        // Create a new <li> element with the text "Item"
        const newItem = $('<li>Item</li>');
        
        // Append the new <li> element to the UL.my_list
        $('ul.my_list').append(newItem);
    });
});
