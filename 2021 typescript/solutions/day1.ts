import * as fs from "fs";

export function solveDay(): number[] {
	const input = fs.readFileSync('input/day1.txt', 'utf8').split('\n');

	let i: number;
	let result1: number = 0;

	for (i = 1; i < input.length; i++) {
		if (input[i - 1] < input[i]) {
			result1++;
		}
	}

	let result2: number = 0;
	let arr: number[] = [];

	for (i = 0; i < input.length; i++) {
		arr.push(parseInt(input[i]) + parseInt(input[i + 1]) + parseInt(input[i + 2]));
	}
	for (i = 0; i < input.length; i++) {
		if (arr[i] < arr[i + 1]) {
			result2++;
		}
	}

	return [result1, result2];
}
