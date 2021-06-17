from utils.annotations import track_performance
from utils.toitientHelpers import o1isPrime, getGCD

def isInRangeAndNotReducible(n,d):
    reducible = getGCD(n,d) != 1
    if reducible:
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
    for i in range(2, 10):
        print('f count i is ', i, getFractionCountInRange(i))

@track_performance
def testFCPerf():
    print('starting perf test for FC')
    for i in range(11900, 12001):
        print('f count i is ', i, getFractionCountInRange(i))

euler73()
# testAbsoluteSort()
# testFractionCount()
testFCPerf()