const test = require('tape');
const findLongestIncreasingPath = require('./index');

test('Longest increasing path in Matrix', (t) => {
  t.equals(0, findLongestIncreasingPath([[]]), 'works on empty arrays');
  t.equals(1, findLongestIncreasingPath([[1]]), 'works on single element matrix');
  t.equals(3, findLongestIncreasingPath([[3], [2], [1]]), 'works on single row matrix');
  t.equals(4, findLongestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]), 'works on bidimensional matrix');
  // t.equals(100, findLongestIncreasingPath([
  //   [0,1,2,3,4,5,6,7,8,9,10],
  //   [19,18,17,16,15,14,13,12,11],
  //   [20,21,22,23,24,25,26,27,28,29,30],
  //   [39,38,37,36,35,34,33,32,31],
  //   [40,41,42,43,44,45,46,47,48,49,50],
  //   [59,58,57,56,55,54,53,52,51],
  //   [60,61,62,63,64,65,66,67,68,69,70],
  //   [79,78,77,76,75,74,73,72,71],
  //   [80,81,82,83,84,85,86,87,88,89,70],
  //   [99,98,97,96,95,94,93,92,91],
  //   [0,0,0,0,0,0,0,0,0]
  // ]), 'works on big arrays');
  t.end();
});
