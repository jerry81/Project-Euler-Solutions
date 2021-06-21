from utils.annotations import track_performance

def getBGivenAAndT(a, t):
    d = t - a
    return (a**2 - d**2) / (-2 * d)

def isWhole(n):
    return int(n) == n

@track_performance
def euler75():
    print('project euler problem 75')

euler75()
