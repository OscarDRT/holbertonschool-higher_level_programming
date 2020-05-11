#!/usr/bin/node

exports.esrever = function (list) {
  const mylist = [];
  list.forEach(element => {
    mylist.unshift(element);
  });
  return mylist;
};
