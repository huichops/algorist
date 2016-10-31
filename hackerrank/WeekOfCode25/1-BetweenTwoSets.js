function main() {
  const [n, m] = readLine().split(' ').map(Number);
  const a = readLine().split(' ').map(Number);
  const b = readLine().split(' ').map(Number);

  const min = Math.max.apply(null, a);
  const max = Math.min.apply(null, b);
  let factors = 0;

  for (let i = min; i <= max; i++) {
    const isFactor = isFactorOf(i);
    const bReduce = b.reduce(isFactor, []);

    if (bReduce.length === m) {
      aReduce = a.reduce((result, n) =>
          isFactorOf(n)(result, i), []);
      if (aReduce.length === n) factors++;
    }
  }

  console.log(factors);
}

const isFactorOf = x => (result, n) => {
  if (n % x === 0) return result.concat(x);
  return result;
}
