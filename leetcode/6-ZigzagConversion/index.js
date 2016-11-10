module.exports = convert = (s, numRows) => {
  if (numRows === 1 || numRows === 0) return s;
  const chars = s.split('')
    const lines = Array.apply(null, {length: numRows}).map(() => '')
    return chars.reduce(zigzag(numRows), lines).join('')
};

const zigzag = (numRows) => {
  let factor = -1;
  let lineIndex = 0;

  return (acc, char, index) => {
    if (!(index % (numRows - 1))) factor *= -1;
    acc[lineIndex] += char;
    lineIndex += factor;
    return acc;
  }
};
