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
const inputRaw = fs.readFileSync('input/day11.txt', 'utf-8').split('\n');
const row = inputRaw[0].length - 1;
const column = inputRaw.length;
let nodes = [];
let result = 0;
function solveDay() {
    console.log('Note: day11 has wrong input data.');
    addNodes();
    for (let rounds = 1; rounds < 3; rounds++) {
        increaseNodes();
        adjacentNodes();
        resetNodes();
    }
    return [result, 0];
}
exports.solveDay = solveDay;
function addNodes() {
    for (let x = 0; x < row; x++) {
        for (let y = 0; y < column; y++) {
            nodes.push({ num: parseInt(inputRaw[x].charAt(y)), coordinates: { x: x, y: y }, flashed: false, flashAdjacent: false });
        }
    }
}
function increaseNodes() {
    for (let i = 0; i < nodes.length; i++) {
        nodes[i].num++;
        if (nodes[i].num > 9) {
            nodes[i].num = 0;
            nodes[i].flashAdjacent = true;
            result++;
        }
    }
}
function adjacentNodes() {
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].flashAdjacent === true && nodes[i].flashed === false) {
            nodes[i].flashed = true;
            checkAdjacents(findAdjacents(i));
        }
    }
}
function findAdjacents(i) {
    let adj = [];
    for (let x = -1; x < 2; x++) {
        for (let y = -1; y < 2; y++) {
            if (x !== 0 || y !== 0) { // don't add the node we're on
                if (isAdjacentsInsideGrid(nodes[i].coordinates, x, y)) { // is inside the grid
                    adj.push({ x: nodes[i].coordinates.x + x, y: nodes[i].coordinates.y + y });
                }
            }
        }
    }
    return adj;
}
function checkAdjacents(adj) {
    for (let i = 0; i < adj.length; i++) {
        for (let j = 0; j < nodes.length; j++) {
            if (isCoordinatesEqual(nodes[j].coordinates, adj[i])) {
                nodes[j].num++;
                if (nodes[j].num > 9) {
                    nodes[j].num = 0;
                    nodes[j].flashAdjacent = true;
                    result++;
                    adjacentNodes();
                }
            }
        }
    }
}
function isAdjacentsInsideGrid(node, x, y) {
    return (node.x + x > -1 && node.x + x < 11) && (node.y + y > -1 && node.y + y < 11);
}
function isCoordinatesEqual(node, adjacent) {
    return node.x === adjacent.x && node.y === adjacent.y;
}
function resetNodes() {
    for (let i = 0; i < nodes.length; i++) {
        nodes[i].flashed = false;
        nodes[i].flashAdjacent = false;
    }
}
/* function forAdjacents(input: number[][], index: number) {
  if (input[1][index] === 0) {
    let adjacentIndex: number[] = [];
    input[1][index] = 1;

    if (index % 10 === 0 && index !== 0) {
      adjacentIndex = [
        index - row - 1,
        index - row,
        index - 1,
        index + row - 1,
        index + row,
      ];
    }

    else if (index === 11 || index === 21 || index === 31 || index === 41 || index === 51 || index === 61 || index === 71 || index === 81 || index === 91) {
        adjacentIndex = [
        index - row,
        index - row + 1,
        index + 1,
        index + row,
        index + row + 1,
      ];
    }

    else {
      adjacentIndex = [
        index - row - 1,
        index - row,
        index - row + 1,
        index - 1,
        index + 1,
        index + row - 1,
        index + row,
        index + row + 1,
      ];
    }

    for (let i = 0; i < adjacentIndex.length; i++) {
      if (adjacentIndex[i] > -1 &&
        adjacentIndex[i] < 101 &&
        adjacentIndex[i] !== undefined &&
        adjacentIndex[i] !== null) {
        input[0][adjacentIndex[i]]++;

        if (input[0][adjacentIndex[i]] > 9) {
          input[0][adjacentIndex[i]] = 0;
          input[1][adjacentIndex[i]] = 1;
          result++;
          flashed.push(adjacentIndex[i]);
        }
      }
    }
  }
} */
/* const inputRaw = fs.readFileSync('input/day11.txt', 'utf-8').split('\n');
const row: number = inputRaw[0].length - 1;
const column: number = inputRaw.length;
let input: number[][] = [[], []];
let flashed: number[] = [];
let result = 0;

export function solveDay(): number[] {
  loadInput();

  for (let rounds = 1; rounds < 101; rounds++) {
    increaseInput();
    for (let i = 0; i < flashed.length; i++) {
      forAdjacents(flashed[i]);
    }
    reset();
  }
  return [result, 0];
}

function loadInput() {
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < column; j++) {
      input[0].push(parseInt(inputRaw[i].charAt(j)));
      input[1].push(0);
    }
  }
}

function increaseInput(){
  for (let index = 0; index < input[0].length; index++) {
    input[0][index]++;

    if (input[0][index] > 9) {
      input[0][index] = 0;
      result++;
      flashed.push(index);
    }
  }
}

function forAdjacents(index: number) {
  if (input[1][index] === 0) {
    let adjacentIndex: number[] = [];
    input[1][index] = 1;

    if (index % 10 === 0 && index !== 0) {
      adjacentIndex = [
        index - row - 1,
        index - row,
        index - 1,
        index + row - 1,
        index + row,
      ];
    }

    else if (index === 11 || index === 21 || index === 31 || index === 41 || index === 51 || index === 61 || index === 71 || index === 81 || index === 91) {
        adjacentIndex = [
        index - row,
        index - row + 1,
        index + 1,
        index + row,
        index + row + 1,
      ];
    }

    else {
      adjacentIndex = [
        index - row - 1,
        index - row,
        index - row + 1,
        index - 1,
        index + 1,
        index + row - 1,
        index + row,
        index + row + 1,
      ];
    }

    for (let i = 0; i < adjacentIndex.length; i++) {
      if (adjacentIndex[i] > -1 &&
        adjacentIndex[i] < 101 &&
        adjacentIndex[i] !== undefined &&
        adjacentIndex[i] !== null) {
        input[0][adjacentIndex[i]]++;

        if (input[0][adjacentIndex[i]] > 9) {
          input[0][adjacentIndex[i]] = 0;
          input[1][adjacentIndex[i]] = 1;
          result++;
          flashed.push(adjacentIndex[i]);
        }
      }
    }
  }
}

function reset() {
  for (let i = 0; i < input[1].length; i++) {
    input[1][i] = 0;
  }
  flashed = [];
}
*/ 
//# sourceMappingURL=day11.js.map