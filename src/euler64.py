from utils.annotations import track_performance
from math import sqrt

def splitDec(num):
    whole = int(num)
    remainder = num - whole
    if remainder == 0:
        return whole, remainder, 0
    nxt = 1/remainder
    return whole, remainder, nxt

def getPattern(num):
    pattern = []
    repeatRemainders = []
    count = 0
    inp = sqrt(num) 
    while True:
      whole, remainder, nxt = splitDec(inp)
      pattern.append(whole)
      remainder = round(remainder, 7)
      if remainder == 0 or remainder in repeatRemainders:
          return repeatRemainders, pattern, count
      repeatRemainders.append(remainder)
      inp = nxt
      count += 1
      if count > 10: 
          return repeatRemainders, pattern[1:], count

@track_performance
def euler64():
    print('project euler problem 64')
    
def testRemainder():
  w, r, n = splitDec(sqrt(2))
  w2, r2, n2 = splitDec(n)
  print('w and r and n are ', w, r, n)
  print('w2, r2, and n2 are ', w2, r2, n2)

def testGetPattern():
    for i in range(14):
        repeats, remainders, count = getPattern(i)
        print('getPattern i is rep, rem, count', i, repeats, remainders, count)

euler64()
testRemainder()
testGetPattern()