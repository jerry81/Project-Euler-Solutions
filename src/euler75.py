from utils.annotations import track_performance

def getBGivenAAndT(a, t):
    d = t - a
    return (a**2 - d**2) / (-2 * d)

def isWhole(n):
    return int(n) == n

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

euler75()
# testIsWhole()
testGetB()