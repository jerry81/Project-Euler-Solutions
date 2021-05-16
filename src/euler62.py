from utils.annotations import track_performance
from utils.myitertools import getPermsOfNumber, getPermsOfNumberOOTB
import math


def testLog():
    print('2 is ', math.log(4, 2))
    print('3 is ', math.log(27, 3))


def isCube(num):
    if num <= 1:
        return False
    l = num ** (1/3)
    return round(l) ** 3 == num


def testCube():
    print('True is ', isCube(27))
    print('False is ', isCube(16))
    print('True is ', isCube(81))
    print('False is ', isCube(82))


def getCubeCount(perms, orig):
    return len(list(
        filter(
            lambda x: isCube(x) and len(str(orig)) == len((str(x))), perms
        )
    ))

def getFingerprint(num):
  asList = list(str(num))
  fpL = [0,0,0,0,0,0,0,0,0,0]
  for i in asList:
    fpL[int(i)] += 1
  return "".join(list(map(lambda x: str(x),fpL)))

def makeCubesMap(limit):
  cm = {}
  for i in range(3, limit):
    k = i**3
    cm[k] = getFingerprint(k)
  return cm

def testGetFingerprint():
  print('fingerprint of 127395882 is ', getFingerprint(127395882))

def testCubeMap():
  print('makeCubeMap 2000', makeCubesMap(2000))

@track_performance
def euler62():
    print('project euler problem 62')
    for i in range(1002,2000):
        cube = i ** 3
        permutations = getPermsOfNumberOOTB(cube)
        noDups = list(set(permutations))
        count = getCubeCount(noDups, cube)
        if count == 5:
            print('i is ', i)
            return


print('345 cubed is ', 345*345*345, 345**3)
print('math log ', math.log(41063625, 3))
print('math exp 1/3', 41063625 ** (1/3))
print('isCube(410...)', isCube(41063625))
print('getCubecount', getCubeCount(
    list(
      set(
          getPermsOfNumber(41063625)
      )
      ),
    41063625))
testLog()
testCube()
testGetFingerprint()
testCubeMap()
# euler62()
