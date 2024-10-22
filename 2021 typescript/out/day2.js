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
function solveDay() {
    const input = fs.readFileSync('input/day2.txt', 'utf-8').split('\n');
    let inputAsString = [];
    let inputAsNumber = [];
    let i = 0;
    for (i = 0; i < input.length; i++) {
        inputAsNumber[i] = parseInt(input[i].split(' ')[1]);
        inputAsString[i] = input[i].split(' ')[0];
    }
    let position = [0, 0, 0, 0];
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
exports.solveDay = solveDay;
//1845455714
//# sourceMappingURL=day2.js.map