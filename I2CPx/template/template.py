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

def countstrokes(keyboard, text):
  strokes = []
  for c in text:
    title, code = c[0], c[1:]
    lastchar = code[0][0]
    total = 0

    for line in code:
      for char in line:
        total += getdistance(keyboard, lastchar, char)
        lastchar = char
    strokes.append((title, total))
  return strokes

def getdistance(keyboard, start, end):
  startpos = []
  endpos = []
  for m, line in enumerate(keyboard):
    if (start in line):
      startpos = m, line.index(start)
    if (end in line):
      endpos = m, line.index(end)

  distance = max([abs(startpos[0] - endpos[0]),  abs(startpos[1] - endpos[1])])
  return distance

with open('template.in', 'r') as input:
  x, y = [int(x) for x in input.readline().split(' ')]
  keyboard = readKeyboard(input, y)
  code = splitcode(input.read().split('\n'))
  strokes = countstrokes(keyboard, code)
  result = min(strokes, key=lambda i: i[1])

  with open('template.out', 'w') as output:
    output.write(str(result[0]) + '\n')
    output.write(str(result[1]) + '\n')
    output.write('\n')
