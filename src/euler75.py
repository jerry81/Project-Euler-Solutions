from utils.annotations import track_performance
from math import sqrt

def getBGivenAAndT(a, t):
    d = t - a
    return (a**2 - d**2) / (-2 * d)

def isWhole(n):
    return int(n) == n

def getSetOfIntegerSides(t):
    returned = []
    limA = int(sqrt(t))
    for i in range(1, limA+1):
        b = getBGivenAAndT(i, t)
        if isWhole(b):
            returned += (i,b,sqrt(i**2+b**2))
    return returned

@track_performance
def euler75():
    print('project euler problem 75')

def testIsWhole():
    print('isWhole 7.0', isWhole(7.0))
    print('isWhole 5/2', isWhole(5/2))
    print('isWhole 6/2', isWhole(6/2))

def testGetB():
    print('getB 3 12', getBGivenAAndT(3, 12))
    print('getB 2 12', getBGivenAAndT(2, 12))
    print('getB 6, 24', getBGivenAAndT(6,24))
    print('getB 20, 120', getBGivenAAndT(20, 120))

def testGetSet():
    print('getSet 12', getSetOfIntegerSides(12))
    print('getSet 24', getSetOfIntegerSides(24))
    print('getSet 30', getSetOfIntegerSides(30))
    print('getSet 36', getSetOfIntegerSides(36))
    print('getSet 40', getSetOfIntegerSides(40))
    print('getSet 48', getSetOfIntegerSides(48))
    print('getSet 120', getSetOfIntegerSides(120))

euler75()
# testIsWhole()
# testGetB()
testGetSet()