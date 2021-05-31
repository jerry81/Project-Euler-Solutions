from utils.annotations import track_performance
from utils.fileUtils import writeArrayToFile, openAndSplit
from euler64 import getNextIter
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
        y += 1

def solvePell(x, y, d):
    return x ** 2 - (d * (y ** 2))


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
    d13 = 13
    d109 = 109
    d661 = 661
    print('solve x 2', solveXDiophantine(d1))
    print('solve x 3', solveXDiophantine(d2))
    print('solve x 5', solveXDiophantine(d3))
    print('solve x 6', solveXDiophantine(d4))
    print('solve x 7', solveXDiophantine(d5))
    print('solve x 13', solveXDiophantine(d13))
"""     print('solve x 661', solveXDiophantine(d661))
    print('solve x 109', solveXDiophantine(d109)) """


def tryI(i):
    repeats = []
    wholes = []
    w = int(sqrt(i))
    wholes.append(w)
    d = 1
    n = w * -1
    pell = solvePell(n, d, i)
    print('pell is ', pell)
    returnedNum = 0
    while pell != 1:
      n, d, w = getNextIter(i, n, d)
      wholes.append(w)
      num, den = getRecurrentFraction(wholes.copy())
      print('num, den are ', num, den)
      pell = solvePell(num, den, i)
      returnedNum = num
    return num

def getRecurrentFraction(series):
    if len(series) == 1:
        return series[0], 1
    print('series is ', series)
    num = 1
    item = series.pop()
    den = item
    while series:
        item = series.pop()
        print('item is ', item)
        newNum = (den * item) + num 
        num = den
        den = newNum
    return den, num

def getMaxInFiles():
    files = ['0to100', '100to200', '201to300', '301to400', '401to500',
             '501to600', '601to700', '701to800', '801to900', '901to1000']
    prefix = './resources/diophantines'
    suffix = '.txt'
    mx = 0
    fx = ''
    for f in files:
        arr = openAndSplit(prefix+f+suffix)
        asF = map(lambda x: float(x), arr)
        tmax = max(asF)
        if tmax > mx:
            mx = tmax
            fx = f
    return mx, fx

def testI():
    print('tryI 7 is ', tryI(7))
    print('solve pell 8, 3, 7 is ', solvePell(8, 3, 7))
    print('tryI 109 is ', tryI(109))

@track_performance
def euler66():
    print('project euler problem 66')
    tmax = 0
    highestIndex = 0
    for i in range(0, 1001):
        if isPerfectSquare(i):
            continue
        cur = tryI(i)
        if cur > tmax:
            highestIndex = i
            tmax = cur
    print('highestIndex ', highestIndex)
    print('tmax ', tmax)


euler66()
# testIsPerfect()
# testSolveX()
# testI()