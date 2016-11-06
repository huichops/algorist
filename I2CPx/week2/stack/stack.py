with open('stack.in', 'r') as input:
  n = input.readline()
  stack = []
  result = []
  for command in input:
    if (command[0] == '+'):
      stack.append(command[2:])
    else:
      result.append(stack.pop())
  with open('stack.out', 'w') as output:
    output.write(''.join(result))
