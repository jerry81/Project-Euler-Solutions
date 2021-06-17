from utils.annotations import track_performance
from utils.toitientHelpers import o1isPrime, getGCD

def isInRangeAndNotReducible(n,d):
    notReducible = getGCD(n,d) == 1
    if notReducible:
        return False
    val = n / d
    inRange = val > 1/3 and val < 1/2
    return inRange 

@track_performance
def euler73():
    print('project euler problem 73')   

def testAbsoluteSort():
    arr = []
    for i in range(2,12001):
      for j in range(1, i):
          arr.append(j/i)
    arr.sort()
    print('arr, sorted is ', arr)
    print('len is ', len(arr))

euler73()
# testAbsoluteSort()