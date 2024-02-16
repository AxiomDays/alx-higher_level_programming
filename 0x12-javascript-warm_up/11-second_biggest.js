#!/usr/bin/node

/* a script that searches the biggest integer in a list of arguments */

if (process.argv.length < 4){
	console.log(0);
} else {
	let temp = process.argv.slice(2);
	temp = temp.sort();
	temp = temp.reverse();
	temp = new Set(temp);
	temp = Array.from(temp);
	console.log(parseInt(temp[1]));
}
