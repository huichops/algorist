module.exports = (matrix) => {

  if (matrix.length === 0) return 0;
  if (matrix[0].length === 0) return 0;

  const m = matrix.length;
  const n = matrix[0].length;
  const memory = [];
  let max = -99999

  for (let p = 0; p < m; p++) {
    memory.push([]);
    for (let q = 0; q < n; q++) {
      memory[p].push(0);
    }
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let path = getLongestPath(matrix, i, j, -1, 0, memory);
      if (path > max) max = path;
    }
  }
  return max;
};

const getLongestPath = (matrix, m, n, number, length, memory) => {
  const coords = [[0, -1], [0, 1], [1, 0], [-1, 0]];
  let max = -9999;

  if (m < 0 || m >= matrix.length) return 0;
  if (n < 0 || n >= matrix[0].length) return 0;
  if (number >= matrix[m][n]) return 0;
  if (memory[m][n]) return memory[m][n];

  for (let i = 0; i < coords.length; i++) {
    let path = getLongestPath(
        matrix, m + coords[i][0],
        n + coords[i][1],
        matrix[m][n],
        length,
        memory) + 1;
    if (path > max) max = path;
  }
  memory[m][n] = max;
  return max;
}
