#!/usr/bin/node
xports.callMeMoby = function (x, callback) {
  for (let i = 0; i < x; i++) {
    callback();
  }
};
