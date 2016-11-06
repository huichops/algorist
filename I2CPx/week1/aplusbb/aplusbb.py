with open('aplusbb.in', 'r') as input:
  a, b = [int(x) for x in input.readline().split(' ')]
  with open('aplusbb.out', 'w') as output:
    output.write(str(a + b * b))
    output.write('\n')
