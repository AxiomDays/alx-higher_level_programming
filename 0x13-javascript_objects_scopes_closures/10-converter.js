#!/usr/bin/node

/* script that turns a base to another */

exports.converter = function (base) {
	function parse (number) {
		return number.toString(base);
	}
	return parse;
}
