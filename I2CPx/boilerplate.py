with open('aplusb.in', 'r') as input:
  a, b = [int(x) for x in input.readline().split(' ')]
  with open('aplusb.out', 'w') as output:
    output.write(str(a + b))
    output.write('\n')
