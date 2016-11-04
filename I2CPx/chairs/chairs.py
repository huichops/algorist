with open('chairs.in', 'r') as input:
  sides  = [int(x) for x in input.readline().split(' ')]
  sidesSum = sum([(x / 2) for x in sides])

  with open('chairs.out', 'w') as output:
    output.write(str(sidesSum / 3))
    output.write('\n')
