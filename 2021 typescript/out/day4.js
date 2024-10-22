"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.solveDay = void 0;
const fs = __importStar(require("fs"));
let allBoards = [];
function solveDay() {
    var _a;
    const inputRaw = fs.readFileSync('input/day4.txt', 'utf-8').split('\n');
    const input = (_a = inputRaw.shift()) === null || _a === void 0 ? void 0 : _a.split(',');
    inputRaw.shift();
    let rowsWIP = [];
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
        allBoards.push({ rows: [], columns: [] });
    }
    // create rows
    let rows = [];
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
        rows.forEach((row, index) => {
            if (board.rows.length > 5) {
                board.rows.push(row);
            }
        });
    });
    //add columns
    let columns = [];
    let column = [];
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
    for (let i = 0; i < input.length; i++) { // !
        // check input
        // mark input on boards, all of them?
        // check for bingo per board
    }
    return [0, 0];
}
exports.solveDay = solveDay;
//# sourceMappingURL=day4.js.map