#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(element => {
    if (searchElement === element) { count += 1; }
  });
  return count;
};
