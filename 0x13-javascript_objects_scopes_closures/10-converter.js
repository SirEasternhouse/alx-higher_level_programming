#!/usr/bin/node

exports.converter = function (base) {
  if (base <= 0 || base > 36) return;

  return function convertRecursive (number) {
    return (number < base) ? number.toString(36).toUpperCase() : convertRecursive(parseInt(number / base)) + (number % base).toString(36).toUpperCase();
  };
};
