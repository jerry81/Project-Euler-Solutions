from utils.annotations import track_performance
from utils.toitientHelpers import o1isPrime, getGCD

def isInRangeAndNotReducible(n,d):
    notReducible = getGCD(n,d) == 1
    if notReducible:
        return False
    val = n / d
    inRange = val > (1/3) and val < (1/2)
    return inRange 

@track_performance
def euler73():
    print('project euler problem 73')
   
def getFractionCountInRange(d):
    count = 0
    start = d // 3
    end = (d // 2) + 2
    for i in range(start, end):
      if isInRangeAndNotReducible(i, d):
          count += 1
    return count

def testAbsoluteSort():
    arr = []
    for i in range(2,12001):
      for j in range(1, i):
          arr.append(j/i)
    arr.sort()
    print('arr, sorted is ', arr)
    print('len is ', len(arr))

def testFractionCount():
    print('f count 8 is ', getFractionCountInRange(8))
    print('f count 9 is ', getFractionCountInRange())

euler73()
# testAbsoluteSort()