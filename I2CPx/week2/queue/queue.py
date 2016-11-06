with open('queue.in', 'r') as input:
  n = input.readline()
  queue = [None] * int(n)
  head = 0
  tail = 0
  result = []
  for command in input:
    if (command[0] == '+'):
      queue[tail] = command[2:]
      tail += 1
    else:
      result.append(queue[head])
      head +=1
  with open('queue.out', 'w') as output:
    output.write(''.join(result))
