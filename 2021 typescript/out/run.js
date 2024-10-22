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
const day1 = __importStar(require("./day1"));
const day2 = __importStar(require("./day2"));
const day3 = __importStar(require("./day3"));
const day4 = __importStar(require("./day4"));
const day5 = __importStar(require("./day5"));
const day6 = __importStar(require("./day6"));
const day7 = __importStar(require("./day7"));
const day8 = __importStar(require("./day8"));
const day9 = __importStar(require("./day9"));
const day10 = __importStar(require("./day10"));
const day11 = __importStar(require("./day11"));
let i = 0;
const days = 11;
const func = [day1.solveDay(), day2.solveDay(), day3.solveDay(), day4.solveDay(), day5.solveDay(), day6.solveDay(), day7.solveDay(), day8.solveDay(), day9.solveDay(), day10.solveDay(), day11.solveDay()];
console.log('Day', 3, ': ', func[3]);
/* for (i = 0; i < days; i++) {
  console.log('Day', i+1, ': ', func[i]);
} */
//# sourceMappingURL=run.js.map