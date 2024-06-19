#!/usr/bin/node

exports.converter = function (base) {
  if (base <= 0 || base > 36) return;

  const convertRecursive = function (number) {
    if (number < base) {
      return number.toString(36).toUpperCase();
    } else {
      return convertRecursive(parseInt(number / base)) + (number % base).toString(36).toUpperCase();
    }
  };

  return convertRecursive;
};
