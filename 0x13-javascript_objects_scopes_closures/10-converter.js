#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (input) {
    return input.toString(base);
  };
};
