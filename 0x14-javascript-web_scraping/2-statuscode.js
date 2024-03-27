#!/usr/bin/node
const fs = require('fs');
const req = require('request');
req(process.argv[2], (err, resp, data) => {
	console.log('code:', resp && resp.statusCode);
})
