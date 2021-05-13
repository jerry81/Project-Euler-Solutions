from utils.annotations import track_performance
from utils.myitertools import getPermsOfNumber
import math
import copy

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

def getPermutationsR(arr):
  if len(arr) == 1:
    return arr
  if len(arr) == 2:
    rev = copy.copy(arr)
    rev.reverse()
    return [arr, rev]
  # isolate first item 
  sub1 = arr[:1][0]
  sub2 = arr[1:]
  permutations = getPermutationsR(sub2)
  expanded = []
  for i in range(len(arr)):
    for idx, p in enumerate(permutations):
      c = copy.copy(p)
      c.insert(i, sub1)
      expanded.append(c)
  return expanded

  print('sub1 sub2 ', sub1, sub2)

def testGetPermutationsR():
  test1 = [1,2]
  test2 = [5,6]
  test3 = [1,2,3]
  test4 = [1,2,3,4]
  print('12 21 is ', getPermutationsR(test1))
  print('56, 65 is ', getPermutationsR(test2))
  print('123, 132, etc... is ', getPermutationsR(test3))
  print('1234, 1243, etc... is ', getPermutationsR(test4))

testLog()
testCube()
euler62()
testGetPermutationsR()