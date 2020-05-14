$(document).ready(() => {
  function say () {
    const leng = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
    $.ajax({
      type: 'GET',
      url: url,
      success: (response) => {
        $('DIV#hello').text(response.hello);
      }
    });
  }

  $('INPUT#btn_translate').click((e) => {
    e.preventDefault();
    say();
  });

  $('INPUT#language_code').keypress(function (e) {
    if (e.which == 13) {
      e.preventDefault();
      say();
    }
  });
});
