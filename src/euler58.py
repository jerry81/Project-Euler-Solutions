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
  start = dim ** 2
  if dim < 1:
    return [[]]
  spiral = [[0]*dim for i in range(dim)]
  for outer in range(dim, -1, -1):
    for x in range(outer, -1, -1):
      spiral[y][outer] = start
      start -= 1
    for h in range(outer, -1, -1):
      spiral[0][]
  return spiral


def testSpirals():
  makeSpirals(1)
  makeSpirals(2)
  makeSpirals(3)

@track_performance
def euler58():
  print('spirals')

euler58()
testSpirals()