import * as day1 from './day1';
import * as day2 from './day2';
import * as day3 from './day3';
import * as day4 from './day4';
import * as day5 from './day5';
import * as day6 from './day6';
import * as day7 from './day7';
import * as day8 from './day8';
import * as day9 from './day9';
import * as day10 from './day10';
import * as day11 from './day11';

let i: number = 0;
const days: number = 11;
const func = [day1.solveDay(), day2.solveDay(), day3.solveDay(), day4.solveDay(), day5.solveDay(), day6.solveDay(), day7.solveDay(),day8.solveDay(), day9.solveDay(), day10.solveDay(), day11.solveDay()];

console.log('Day', 3, ': ', func[3]);

/* for (i = 0; i < days; i++) {
  console.log('Day', i+1, ': ', func[i]);
} */
