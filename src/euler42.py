print('project euler problem 42')

charDict = {
  'a': 1, 'b': 2, 'c': 3,
  'd': 4, 'e': 5, 'f': 6,
  'g': 7, 'h': 8, 'i': 9,
  'j': 10, 'k': 11, 'l': 12,
  'm': 13, 'n': 14, 'o': 15,
  'p': 16, 'q': 17, 'r': 18, 
  's': 19, 't': 20, 'u': 21,
  'v': 22, 'w': 23, 'x': 24,
  'y': 25, 'z': 26
}

def getTriangles(numOfEntries):
  returned = []
  for i in range(0, numOfEntries):
    returned.append(int(.5 * i * (i+1)))
  return returned

trianglesList = getTriangles(10000)
def filterCommas(item):
  return item != ',' and item != ''

def getStrValue(input):
  lower = input.lower()
  total = 0
  for i in range(0, len(input)):
    char = lower[i]
    total += charDict[char]
  return total

reader = open('./resources/p042_words.txt')
try: 
  inputStr = reader.read()
  filtered = list(filter(filterCommas, inputStr.split('"')))
  print('inputArr', len(filtered))
  count = 0
  for i in range(0, len(filtered)):
    cand = getStrValue(filtered[i])
    print('cand is ', cand)
    if cand in trianglesList:
      count += 1
  print('count is ', count)
finally:
  reader.close()

