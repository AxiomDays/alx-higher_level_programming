$.ajax({url: "https://swapi-api.alx-tools.com/api/people/5/?format=json", success: function(result){
    $("div#character").html(result.name);
  }});
