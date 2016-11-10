def validatebrackets(string):
  stack = []
  for char in string:
    if (char == '('): stack.append(1)
    if (char == ')' and len(stack) and stack[-1] == 1): stack.pop()
    if (char == '['): stack.append(2)
    if (char == ']' and len(stack) and stack[-1] == 2): stack.pop()

  if (len(stack)): return False
  return True

with open('brackets.in', 'r') as input:
  result = ''
  for line in input:
     answer = 'YES' if validatebrackets(line) else 'NO'
     result += answer + '\n'
  with open('brackets.out', 'w') as output:
    output.write(result)
    output.write('\n')
