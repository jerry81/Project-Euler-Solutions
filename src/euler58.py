from utils.annotations import track_performance

print('project euler problem 58')

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
  print('dim is ', dim)
  print('start is ', start)
  midpoint = int(dim / 2)
  direction = 'L'
  print('mid is ', midpoint)
  x = maxDim
  y = maxDim
  if dim < 1:
    return [[]]
  spiral = [[0]*dim for i in range(dim)]
  while start > 0:
    if direction == 'L':
      while x >= minDim:
        print('x y is ', x, y)
        spiral[y][x] = start 
        x -= 1
        start -= 1
      x += 1
      y -= 1
      direction = 'U'
    elif direction == 'U':
      while y >= minDim:
        print('x y is ', x, y)
        spiral[y][x] = start 
        y -= 1
        start -= 1
      x += 1
      y += 1
      direction = 'R'
    elif direction == 'R':
      while x <= maxDim:
        print('x y is ', x, y)
        spiral[y][x] = start 
        x += 1
        start -= 1
      x -= 1
      y += 1
      direction = 'D'
    else: 
      while y <= maxDim - 1:
        print('x y is ', x, y)
        spiral[y][x] = start 
        print('x, y set to ', start)
        y += 1
        start -= 1
      y -= 1
      x -= 1
      minDim += 1
      maxDim -= 1
      direction = 'L'
      print('x, y after one full', x, y)
  print('spiral is ', spiral)
  return spiral

def testSpirals():
  makeSpirals(1)
  makeSpirals(2)
  makeSpirals(3)
  # makeSpirals(4)

@track_performance
def euler58():
  print('spirals')

euler58()
testSpirals()