const test = require('tape');
const zigzagConversion = require('./index');

test('Zigzag Conversion', (t) => {
  t.equals('', zigzagConversion('', 0), 'works on empty strings');
  t.equals('PAYPALISHIRING', zigzagConversion('PAYPALISHIRING', 0), 'works with 0 rows');
  t.equals('PAYPALISHIRING', zigzagConversion('PAYPALISHIRING', 1), 'works with 1 rows');
  t.equals('PAHNAPLSIIGYIR', zigzagConversion('PAYPALISHIRING', 3), 'works with many rows');
  t.end();
});
