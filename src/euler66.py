from utils.annotations import track_performance
from math import sqrt

def isPerfectSquare(x):
  return int(sqrt(x)) == sqrt(x)

def testIsPerfect():
    print('isperfect 17', isPerfectSquare(17))
    print('isperfect 16', isPerfectSquare(16))
    print('isperfect 4', isPerfectSquare(4))

@track_performance
def euler66():
    print('project euler problem 66')
    
euler66()
testIsPerfect()