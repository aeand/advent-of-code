import * as fs from 'fs';

const inputRaw = fs.readFileSync('input/day3.txt', 'utf-8').split('\n');
const row: number = inputRaw.length;
const column: number = inputRaw[0].length-1;
let counter: number[] = [];

export function solveDay(): number[] {
  createCounter();
  countBits();
  const gammaRate = getGammaRate();
  const epsilonRate = getEpsilonRate(gammaRate)
  const oxygenRate = getOxygenRate();
  const scrubberRate = getScrubberRate();

  return [parseInt(gammaRate, 2) * parseInt(epsilonRate, 2), parseInt(oxygenRate, 2) * parseInt(scrubberRate, 2)];
}

function createCounter() {
  for (let i = 0; i < column; i++) {
    counter.push(0);
  }
}

function countBits() {
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < column; j++) {
      if (inputRaw[i].charAt(j) === '0') {
        counter[j] -= 1;
      }
      else {
        counter[j] += 1;
      }
    }
  }
}

function getGammaRate(): string {
  let counterCommonBinary: string = '';

  for (let i = 0; i < column; i++) {
    if (counter[i] > 0) {
      counterCommonBinary = counterCommonBinary + '1';
    }
    else if (counter[i] < 0) {
      counterCommonBinary = counterCommonBinary + '0';
    }
    else if (counter[i] === 0) {
      counterCommonBinary = counterCommonBinary + 'panic';
    }
  }

  return counterCommonBinary;
}

function getEpsilonRate(input: string): string {
  let counterLeastBinary = '';

  for (let i = 0; i < input.length; i++) {
    if (input.charAt(i) === '0') {
      counterLeastBinary = counterLeastBinary + '1';
    }
    else {
      counterLeastBinary = counterLeastBinary + '0';
    }
  }

  return counterLeastBinary;
}

function coolAttemptButCompletelyWrong(): string {
  let bitString: string = '';
  for (let i = 0; i < column; i++) {
    const temp = counter[i] < 0 ? '0' : '1';
    bitString = bitString + temp;
  }

  return bitString; // should be 101111001110 and 010000110001 for scrubber
}

function getRateAddToNewList() {
/*   let removeList: string[] = [];
  let input: string[] = [];

  for (let i = 0; i < row; i++) {
    input.push(inputRaw[i]);
  }

  for (let i = 0; i < column; i++) {
    const bit = counter[i] < 0 ? '0' : '1';

    for (let j = 0; j < row; j++) {
      const inputa = input[j].charAt(i);

      if (inputa !== bit) {
        removeList.push()
      }
    }
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < column; j++) {
      const removeBit = counter[j] < 0 ? '0' : '1';

      if (inputRaw[i].charAt(j) === removeBit) {
        addList.push(inputRaw[i]);
        console.log(i, j, inputRaw[i], inputRaw[i].charAt(j), counter[j], removeBit);
      }
    }
  }

  return ''; */
}

function getOxygenRate(): string {
  let input: string[] = [];

  for (let i = 0; i < row; i++) {
    input.push(inputRaw[i]);
  }

  // OxygenRate
  for (let i = 0; i < column; i++) {
    const keepZero = counter[i] < 0 ? true : false;
    const keepOne = (counter[i] > 0 || counter[i] === 0) ? true : false;

    for (let j = input.length-1; j > 0; j--) {
      const inputBit = input[j].charAt(i);

      if(keepZero && !(inputBit === '0') || (keepOne && !(inputBit === '1'))) {
        input.splice(j, 1);
      }
    }
  }

  //console.log(input);
  return input[0];
}

function getScrubberRate(): string {
  let input: string[] = [];

  for (let i = 0; i < row; i++) {
    input.push(inputRaw[i]);
  }

  // ScrubberRate
  for (let i = 0; i < column; i++) {
    const keepZero = (counter[i] > 0 || counter[i] === 0) ? true : false;
    const keepOne = counter[i] < 0 ? true : false;

    for (let j = input.length-1; j > 0; j--) {
      const bit = input[j].charAt(i);

      if(keepZero && !(bit === '0') || (keepOne && !(bit === '1'))) {
        input.splice(j, 1);
      }
    }
  }

  //console.log(input);
  return input[0];
}
