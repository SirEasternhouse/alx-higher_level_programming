#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg, 10));
  const uniqueNumbers = [...new Set(numbers)];

  if (uniqueNumbers.length < 2) {
    console.log(0);
  } else {
    uniqueNumbers.sort((a, b) => b - a);
    console.log(uniqueNumbers[1]);
  }
}
