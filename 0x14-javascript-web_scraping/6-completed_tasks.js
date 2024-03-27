#!/usr/bin/node
const fs = require('fs');
const req = require('request');


req.get(process.argv[2], (err, resp, body) => {
	const completed = {};
	todos = JSON.parse(body)
	todos.forEach((todo) => {
		if (todo.completed && completed[todo.userId] === undefined) {
			completed[todo.userId] = 1;
		} else if (todo.completed) {
			completed[todo.userId] += 1;
		}
	});
	console.log(completed);
})
