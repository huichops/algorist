import math

def pow2(x): return x ** 2
def splitLine(line): return [int(x) for x in line.split(' ')]

with open('team.in', 'r') as input:
  andrew = list(map(pow2, splitLine(input.readline())))
  peter = list(map(pow2, splitLine(input.readline())))
  paul = list(map(pow2, splitLine(input.readline())))

  sums = []

  for i in range(0, 3):
    for j in range(0, 3):
      for k in range(0, 3):
        if (i != j and i != k):
          if (i != j and i != k and j != k):
            sums.append(andrew[i] + peter[j] + paul[k])

  result = math.sqrt(max(sums))

  with open('team.out', 'w') as output:
    output.write(str(result))
    output.write('\n')
