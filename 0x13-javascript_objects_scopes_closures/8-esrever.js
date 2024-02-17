#!/usr/bin/node

/* a function that returns the reversed version of a list */

exports.esrever = function (list) {
	let newarr = [];
	for (let i = (list.length - 1); i >= 0; i--) {
		newarr.push(list[i]);
	}
	return newarr;
}
