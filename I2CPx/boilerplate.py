with open('input.in', 'r') as input:
  a, b = [int(x) for x in input.readline().split(' ')]
  with open('output.out', 'w') as output:
    output.write(str(a + b))
    output.write('\n')
