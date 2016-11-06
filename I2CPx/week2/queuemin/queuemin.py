with open('queuemin.in', 'r') as input:
  n = input.readline()
  queue = [None] * int(n)
  head = 0
  tail = 0
  result = []
  mins = [999999999]
  for command in input:
    inst = command[0]
    if (inst == '+'):
      number = int(command[2:])
      if (number < mins[-1]): mins.append(number)
      queue[tail] = number
      tail += 1
    elif (inst == '-'):
      if (mins[-1] == queue[head]): mins.pop()
      if (queue[head] < mins[-1]): mins.append(number)
      head +=1
    else:
      result.append(str(mins[-1]))
  with open('queuemin.out', 'w') as output:
    output.write('\n'.join(result))
    output.write('\n')
