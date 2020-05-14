$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: (response) => {
    const movies = response.results;
    $.each(movies, (index, movie) => {
      const item = $('<li></li>').text(movie.title);
      $('UL#list_movies').append(item);
    });
  }
});
