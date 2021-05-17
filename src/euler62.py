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
  print('fingerPrint of 41063625 is ', getFingerprint(41063625))
  print('fingerprint of 56623104 is ', getFingerprint(56623104))
  print('fingerprint of 66430125 is ', getFingerprint(66430125))

def testCubeMap():
  cubeMap = makeCubesMap(2000)
  print('getCubemap 41063625', cubeMap.get(41063625))
  print('getCubeMap 56623104', cubeMap.get(56623104))
  print('getCubeMap 66430125', cubeMap.get(66430125))

def testFPMap():
  fpMap = makeFingerPrintMap(makeCubesMap(2000))
  # print('fpMap is ', fpMap)
  print('41063625 is ', fpMap['1111112000'])

def makeFingerPrintMap(cubeMap):
  fpMap = {}
  for i in cubeMap:
    val = cubeMap[i]
    if fpMap.get(val, None) !=  None:
      fpMap[val].append(i)
    else:
      fpMap[val] = [i]
  return fpMap

@track_performance
def euler62():
    print('project euler problem 62')
    fp = makeFingerPrintMap(makeCubesMap(20000))
    for k in fp:
      v = fp[k]
      if len(v) == 5:
        print('v is ', v)


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
testFPMap()
euler62()
