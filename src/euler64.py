from utils.annotations import track_performance
from math import sqrt

def splitDec(num):
    whole = int(num)
    remainder = num - whole
    if remainder == 0:
        return whole, remainder, 0
    nxt = 1/remainder
    return whole, remainder, nxt

def oddPeriod(arr):
    return len(arr) % 2 == 1

def getPattern(num):
    pattern = []
    repeatRemainders = []
    count = 0
    inp = sqrt(num) 
    while True:
      whole, remainder, nxt = splitDec(inp)
      pattern.append(whole)
      remainder = round(remainder, 8)
      if remainder == 0 or remainder in repeatRemainders:
          return repeatRemainders, pattern[1:], count
      repeatRemainders.append(remainder)
      inp = nxt
      count += 1
      if count > 1000:
          return repeatRemainders, pattern[1:], count

def getNextIter(i, n, d):
    newN = n * -1
    newTop = sqrt(i) + newN
    newD = (i - n ** 2) / d
    whole = int( newTop / newD )
    newN = newN - (newD * whole)
    return newN, newD, whole

def getResult(i):
    repeats = []
    wholes = []
    w = int(sqrt(i))
    d = 1
    n = w * -1
    n, d, w = getNextIter(i, n, d)
    while (n, d) not in repeats:
        repeats.append((n, d))
        wholes.append(w)
        n, d, w = getNextIter(i, n, d)
    return repeats, wholes

@track_performance
def euler64():
    print('project euler problem 64')
    oddCount = 0
    for i in range(10001):
        repeats, wholes = getResult(i)
        if oddPeriod(wholes):
            oddCount += 1
    print('oddCount is ', oddCount)
    
def testRemainder():
  w, r, n = splitDec(sqrt(2))
  w2, r2, n2 = splitDec(n)
  print('w and r and n are ', w, r, n)
  print('w2, r2, and n2 are ', w2, r2, n2)

def testGetPattern():
    oddCount = 0
    for i in range(50):
        repeats, remainders, count = getPattern(i)
        if oddPeriod(remainders):
            oddCount += 1
        print('getPattern i is rep, rem, count, oddCount', i, repeats, remainders, count, oddCount)

def testTupleComparison():
    t1 = (5, 7)
    t2 = (7, -2)
    t3 = (5,7)
    print('False is ', t1 == t2)
    print('True is ', t1 == t3)

def testGetNextIter():
    n1, d1, w = getNextIter(43, -6, 1)
    print('43, -1, 7 are ', n1, d1, w)
    n2, d2, w2 = getNextIter(43, n1, d1)
    print('43, -5, 6 are ', n2, d2, w2)

def testTupleSearch():
    t1 = (5, 7)
    t2 = (7, -2)
    t3 = (5,7)
    t4 = (8, 8)
    ta = [t1, t2]
    print('True is ', t3 in ta)
    print('False is ', t4 in ta)

def testResult():
    repeats, wholes = getResult(43)
    print('result of 43 is ', repeats, wholes)

euler64()
# testRemainder()
# testGetPattern()
# testTupleComparison()
# testTupleSearch()
# testGetNextIter()
# testResult()