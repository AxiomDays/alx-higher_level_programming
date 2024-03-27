#!/usr/bin/node
const fs = require('fs');
const req = require('request');

const url = ('https://swapi-api.alx-tools.com/api/films/' + process.argv[2]);
req.get(url, (err, resp, body) => {
	console.log(JSON.parse(body).title);
})
