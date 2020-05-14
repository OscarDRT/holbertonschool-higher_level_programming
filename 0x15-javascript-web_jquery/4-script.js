$('DIV#toggle_header').click(() => {
  if ($('header').is('.green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
});
