from utils.annotations import track_performance
from utils.fileUtils import writeArrayToFile, openAndSplit
from math import sqrt

def isPerfectSquare(x):
  return int(sqrt(x)) == sqrt(x)

def solveXDiophantine(d):
    if isPerfectSquare(d):
        return 0
    y = 1
    while True:
      attempt = 1 + (d * (y ** 2))
      if isPerfectSquare(attempt):
          return sqrt(attempt)
      y +=1
    
def testIsPerfect():
    print('isperfect 17', isPerfectSquare(17))
    print('isperfect 16', isPerfectSquare(16))
    print('isperfect 4', isPerfectSquare(4))

def testSolveX():
  d1 = 2
  d2 = 3
  d3 = 5
  d4 = 6
  d5 = 7
  d13 = 13
  d109 = 109
  d661 = 661
  print('solve x 2', solveXDiophantine(d1))
  print('solve x 3', solveXDiophantine(d2))
  print('solve x 5', solveXDiophantine(d3))
  print('solve x 6', solveXDiophantine(d4))
  print('solve x 7', solveXDiophantine(d5))
  print('solve x 13', solveXDiophantine(d13))
  print('solve x 661', solveXDiophantine(d661))
  print('solve x 109', solveXDiophantine(d109))


def getMaxInFiles():
  files = ['0to100', '100to200', '201to300', '301to400', '401to500', '501to600', '601to700', '701to800', '801to900', '901to1000']
  prefix = './resources/diophantines'
  suffix = '.txt'
  mx = 0
  fx = ''
  for f in files:
    arr = openAndSplit(prefix+f+suffix)
    asF = map(lambda x: float(x), arr)
    tmax = max(asF)
    if tmax > mx:
        mx = tmax
        fx = f
  return mx, fx


@track_performance
def euler66():
    print('project euler problem 66')
    print('max is ', getMaxInFiles())
    
euler66()
# testIsPerfect()
testSolveX()