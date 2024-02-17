#!/usr/bin/node

/* a function that returns the number of occurences */

exports.nbOccurences = function (list, searchElement) {
	let count = 0;
	for (let i = 0; i < list.length; i++) {
		if (list[i] === searchElement){
			count++;
		}
	}
	return count;
}
