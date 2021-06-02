from utils.annotations import track_performance
from utils.mathHelpers import getFactors, isPrime

factorsMap = {}

def getFactorsWithout1(n):
    try:
        f = factorsMap[n]
        return f
    except:
        factors = getFactors(n)
        factors.pop(0)
        factorsMap[n] = factors
        return factors


def hasCommon(a,b):
  for i in a:
      if i in b:
          return True
  return False

def getRelativePrimes(n):
    if isPrime(n):
        rps = list(range(n))
        rps.pop(0)
        return rps
    factorsOfN = getFactorsWithout1(n)
    factorsMap[n] = factorsOfN
    rp = []
    for i in range(1,n):
        factorsOfI = getFactorsWithout1(i)
        if not hasCommon(factorsOfI, factorsOfN):
          rp.append(i)
    return rp
        

@track_performance
def euler69():
    print('project euler problem 69')

def testFactors():
    print('factors without 1 27', getFactorsWithout1(27))
    print('factors without 1 42', getFactorsWithout1(42))
    print('factors without 1 42', getFactorsWithout1(42))

def testRp():
    for i in range(2,11):
        print('testRP i is ', i, getRelativePrimes(i))

euler69()
# testFactors()
testRp()