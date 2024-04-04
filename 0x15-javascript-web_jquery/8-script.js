$.ajax({url: "https://swapi-api.alx-tools.com/api/films/?format=json", success: function(result){
	for (i = 0; i < result["results"].length; i++){
	console.log(i);
	console.log(result["results"][i].title);
	$("ul#list_movies").append(`<li> ${result["results"][i].title} </li>`);
	};
  }});
