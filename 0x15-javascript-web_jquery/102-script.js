$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const leng = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
    $.ajax({
      type: 'GET',
      url: url,
      success: (response) => {
        $('DIV#hello').text(response.hello);
      }
    });
  });
});
