#!/usr/bin/node
const fs = require('fs');
const req = require('request');


req.get(process.argv[2], (err, resp, body) => {
	fs.writeFile(process.argv[3], body.toString(), 'utf-8', (err) => {
        if (err) throw err;
})
})
