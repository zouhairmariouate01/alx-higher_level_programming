$(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', function () {
    $('ul.my_list').children().remove();
  });
});
