def readKeyboard(input, size):
  keyboard = []
  for i in range(0, y):
    keyboard.append(input.readline()[:-1])

  input.readline()
  return keyboard

def splitcode(lines):
  entries = []
  index = 0
  while index < len(lines):
    index = lines.index('')
    entries.append(lines[:index])
    lines = lines[index + 1:]

  return entries

def countstrokes(keyboard, code):
  title, code = code[0], code[1:]

with open('template.in', 'r') as input:
  x, y = [int(x) for x in input.readline().split(' ')]
  keyboard = readKeyboard(input, y)
  code = splitcode(input.read().split('\n'))

  # with open('aplusb.out', 'w') as output:
  #   output.write(str(a + b))
  #   output.write('\n')
