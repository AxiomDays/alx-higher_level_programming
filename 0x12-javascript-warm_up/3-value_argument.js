#!/usr/bin/node

/* script that prints the first argument sent to it */

if (typeof(process.argv[2]) !== 'undefined') {
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
