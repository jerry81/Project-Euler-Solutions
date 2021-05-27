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
  print('solve x 2', solveXDiophantine(d1))
  print('solve x 3', solveXDiophantine(d2))
  print('solve x 5', solveXDiophantine(d3))
  print('solve x 6', solveXDiophantine(d4))
  print('solve x 7', solveXDiophantine(d5))

def getMaxInFiles():
  files = ['701to800.txt', '701to800.txt', '701to800.txt', '701to800.txt', '701to800.txt', '701to800.txt', '701to800.txt', '701to800.txt']

@track_performance
def euler66():
    print('project euler problem 66')
    solutions = []
    for i in range(701, 801):
        x = solveXDiophantine(i)
        solutions.append(x)
    print('solutions is ', solutions)
    writeArrayToFile('./resources/diophantines701to800.txt', solutions)
    
euler66()
# testIsPerfect()
# testSolveX()