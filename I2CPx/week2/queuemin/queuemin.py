from collections import deque

with open('queuemin.in', 'r') as input:
  n = input.readline()
  queue = deque([])
  mins = deque([])
  result = []

  for command in input:
    inst = command[0]
    if (inst == '+'):
      number = int(command[2:])
      queue.append(number)
      if (not len(mins) or number < mins[-1]): mins.append(number)
    elif (inst == '-'):
      number = queue.popleft()
      if (number == mins[0]): mins.popleft()
      if (not len(mins) and len(queue)): mins.append(min(queue))
    else:
      result.append(str(mins[-1]))

  with open('queuemin.out', 'w') as output:
    output.write('\n'.join(result))
    output.write('\n')
