with open('prepare.in', 'r') as input:
  n = int(input.readline())
  p = [int(x) for x in input.readline().split(' ')]
  t = [int(x) for x in input.readline().split(' ')]
  power = 0
  minDiff = 99999
  hasRead = False
  hasPractice = False

  for i in range(0, n):
    diff = abs(p[i] - t[i])
    if (minDiff > diff): minDiff = diff
    if (p[i] > t[i]):
      hasPractice = True
      power += p[i]
    else:
      hasRead = True
      power += t[i]
  if (not hasPractice or not hasRead): power -= minDiff

  with open('prepare.out', 'w') as output:
    output.write(str(power))
    output.write('\n')
