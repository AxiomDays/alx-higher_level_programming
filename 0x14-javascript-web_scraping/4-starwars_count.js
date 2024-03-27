#!/usr/bin/node
const fs = require('fs');
const req = require('request');

let count = 0
const url = ('https://swapi-api.alx-tools.com/api/films/');

req.get(url, (err, resp, body) => {
	for (i=0; i<(JSON.parse(body)["results"]).length; i++)
	{
		for (j=0; j<(JSON.parse(body)["results"][i]["characters"]).length; j++)
		{
			if (JSON.parse(body)["results"][i]["characters"][j] == "https://swapi-api.alx-tools.com/api/people/18/"){
				count++;
			}
		}
	}
	console.log(count);
})
