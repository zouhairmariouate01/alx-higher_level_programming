$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('div#hello').html(data.hello);
});
