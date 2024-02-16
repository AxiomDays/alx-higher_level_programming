#!/usr/bin/node

/* a script that computes and prints a factorial */

function factorial(a){
	if (a > 0){
		return a * factorial(a - 1);
	} else {
		return 1;
	}
}

if (!isNaN(parseInt(process.argv[2]))){
	console.log(factorial(parseInt(process.argv[2])));
} else {
	console.log(1);
}
