from utils.annotations import track_performance
from utils.fileUtils import openAndSplit
from utils.mathHelpers import isPrime

print('project euler problem 58')

raw = openAndSplit('./resources/primesTo20M.txt')

# 1
# 5 4 3
# 6 1 2
# 7 8 9 
# 17 16 15 14 13
# 18 5  4  3  12 
# 19 6  1  2  11 
# 20 7  8  9  10 
# 21 22 23 24 25
def makeSpirals(iterations):
  dim = iterations * 2 - 1
  minDim = 0
  maxDim = dim - 1
  start = dim ** 2
  midpoint = int(dim / 2)
  direction = 'L'
  x = maxDim
  y = maxDim
  if dim < 1:
    return [[]]
  spiral = [[0]*dim for i in range(dim)]
  while start > 0:
    if direction == 'L':
      while x >= minDim:
        spiral[y][x] = start 
        x -= 1
        start -= 1
      x += 1
      y -= 1
      direction = 'U'
    elif direction == 'U':
      while y >= minDim:
        spiral[y][x] = start 
        y -= 1
        start -= 1
      x += 1
      y += 1
      direction = 'R'
    elif direction == 'R':
      while x <= maxDim:
        spiral[y][x] = start 
        x += 1
        start -= 1
      x -= 1
      y += 1
      direction = 'D'
    else: 
      while y <= maxDim - 1:
        spiral[y][x] = start 
        y += 1
        start -= 1
      y -= 1
      x -= 1
      minDim += 1
      maxDim -= 1
      direction = 'L'
  return spiral

def getDiagonals(spiral):
  diagonals = set()
  dim = len(spiral[0])
  for i in range(dim):
    diagonals.add(spiral[i][i])
  for i in range(dim):
    diagonals.add(spiral[i][dim - i - 1])
  return diagonals

primes = list(map(lambda x: int(x), raw))
def getRatioOfPrimesOnDiagonal(diagonals):
  primeDiags = list(filter(lambda x: isPrime(x), list(diagonals)))
  return len(primeDiags) / len(list(diagonals))

def testSpirals():
  makeSpirals(1)
  makeSpirals(2)
  makeSpirals(3)
  makeSpirals(4)

def testGetDiagonals():
  four = makeSpirals(4)
  print(getDiagonals(four))

def testGetRatioOfPrimesOnDiagonal():
  four = makeSpirals(4)
  diags = getDiagonals(four)
  print('ratio is 62', getRatioOfPrimesOnDiagonal(diags))
  five = makeSpirals(5)
  diags = getDiagonals(five)
  six = makeSpirals(6)
  diags = getDiagonals(six)

@track_performance
def euler58():
  print('spirals')
  ratio = 1
  iterations = 13120
  while ratio >= 0.1:
    spiral = makeSpirals(iterations)
    iterations += 1
    diags = getDiagonals(spiral)
    ratio = getRatioOfPrimesOnDiagonal(diags)
    print('iterations is ', iterations)
    print('ratio is ', ratio)
  print('iterations is ', iterations)

testSpirals()
testGetDiagonals()
testGetRatioOfPrimesOnDiagonal()
euler58()