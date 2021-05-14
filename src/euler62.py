from utils.annotations import track_performance
from utils.myitertools import getPermsOfNumber, getPermutationsR, getPermsOfNumberOOTB
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


@track_performance
def euler62():
    print('project euler problem 62')
    for i in range(20000):
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
euler62()
