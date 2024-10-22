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
    const input = fs.readFileSync('input/day1.txt', 'utf8').split('\n');
    let i;
    let result1 = 0;
    for (i = 1; i < input.length; i++) {
        if (input[i - 1] < input[i]) {
            result1++;
        }
    }
    let result2 = 0;
    let arr = [];
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
exports.solveDay = solveDay;
//# sourceMappingURL=day1.js.map