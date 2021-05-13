from utils.annotations import track_performance
from utils.fileUtils import openMap
import math

def testLog():
  print('2 is ', math.log(4,2))
  print('3 is ', math.log(27, 3))

def isCube(num):
  l = math.log(num, 3)
  return l == int(l)

def testCube():
  print('True is ', isCube(27))
  print('False is ', isCube(16))
  print('True is ', isCube(81))
  print('False is ', isCube(82))
  

@track_performance
def euler62():
  print('project euler problem 62')

testLog()
testCube()
euler62()
