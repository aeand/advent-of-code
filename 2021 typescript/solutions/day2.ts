import * as fs from 'fs';

export function solveDay(): number[] {
  const input = fs.readFileSync('input/day2.txt', 'utf-8').split('\n');

  let inputAsString: string[] = [];
  let inputAsNumber: number[] = [];
  let i: number = 0;

  for (i = 0; i < input.length; i++) {
    inputAsNumber[i] = parseInt(input[i].split(' ')[1]);
    inputAsString[i] = input[i].split(' ')[0];
  }

  let position: number[] = [0, 0, 0, 0];

  for (i = 0; i < input.length; i++) {
    if (inputAsString[i] === 'up') {
      position[1] -= inputAsNumber[i];
    }
    if (inputAsString[i] === 'down') {
      position[1] += inputAsNumber[i];
    }
    if (inputAsString[i] === 'forward') {
      position[0] += inputAsNumber[i];
      position[2] += inputAsNumber[i];

      if (position[1] !== 0) {
        position[3] += inputAsNumber[i] * position[1];
      }
    }
  }

  return [position[0] * position[1], position[2] * position[3]];
}
//1845455714