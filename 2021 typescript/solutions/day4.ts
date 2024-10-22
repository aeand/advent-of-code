import * as fs from "fs";

interface board {
  rows: string[][];
  columns: string[];
}

let allBoards: board[] = [];

export function solveDay(): number[] {
  const inputRaw = fs.readFileSync('input/day4.txt', 'utf-8').split('\n');

  const input = inputRaw.shift()?.split(',');
  inputRaw.shift();

  let rowsWIP: string[][] = [];
  for (let i = 0; i < inputRaw.length; i + 5) {
    rowsWIP.push(inputRaw.slice(0, 5));
    inputRaw.shift();
    inputRaw.shift();
    inputRaw.shift();
    inputRaw.shift();
    inputRaw.shift();
    inputRaw.shift();

    // could turn a board into a 1D array and add that into boards
    // make input simpler and code harder
  }

  // create board
  for (let i = 0; i < rowsWIP.length; i++) {
    allBoards.push({ rows: [], columns: [] })
  }

  // create rows
  let rows: string[][] = [];
  rowsWIP.forEach(board => {
    board.forEach(row => {
      const boardInRows = row.split(' ');
      boardInRows.forEach((input, index) => {
        if (input === '') {
          boardInRows.splice(index, 1);
        }
      });
      rows.push(boardInRows);
    });
  });

  // add rows to board
  allBoards.forEach(board => {
    rows.forEach((row, index) => { // try to make it add only 5 rows for each board
      if (index > index + 5) {
        //break;
      }
      board.rows.push(row);
      board.rows.push(row);
      board.rows.push(row);
      board.rows.push(row);
      board.rows.push(row);
    })
  })

  //add columns
  let columns: string[][] = [];
  let column: string[] = [];
  for (let i = 0; i < rowsWIP.length; i++) { // board
    for (let j = 0; j < rowsWIP[i].length; j++) { // row
      for (let k = 0; k < rowsWIP[i][j].length; k++) { // char
        const rowNumberArray = rowsWIP[i][j].split(' ');
        column.push(rowNumberArray[k]);
      }
    }
    columns.push(column);
  }
  // add char to column in strange ways

  // don't remember what this is even
  /*   for (let i = 0; i < allBoards.length; i++) {
      allBoards[i].rows = [rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4]];
      allBoards[i].columns = [];
    } */

  // turn every board into a row and column
  // already have rows, could add columms the same way I've added rows and have two arrays
  // could add the first boards rows and columns to boards[0][rows][columns], have to update both at the same time in that case
  // could be worth to keep track of one number per board, aka. find another way to check rows and columns
  // 1D array per board? and x & y method?

  // bingo
  for (let i = 0; i < input!.length; i++) { // !
    // check input
    // mark input on boards, all of them?
    // check for bingo per board
  }

  return [0, 0];
}