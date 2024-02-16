#!/usr/bin/node

/* script that prints the first argument sent to it */

if (process.argv.length === 2) {
        console.log("No argument");
} else if (process.argv.length > 2){
	console.log(process.argv[2]);
}
