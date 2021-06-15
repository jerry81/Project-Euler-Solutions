from utils.mathHelpers import getFactors
import json
from utils.toitientHelpers import o1isPrime, primeMap
from utils.annotations import track_performance

print('generating file')

# 10000 to 100000 primes
# find primes with repeated digits 

factorMap = {}
for i in range(2, 10):
    factors = []
    if o1isPrime(i):
        factors = []
    else:
        factors = list(set(getFactors(i)))
        factors.sort()
        factors.pop(0)
        factors.pop()
    factorMap[i] = factors
print('factorMap is ', factorMap)

@track_performance
def oneM():
    primeFactors = []
    for i in primeMap.keys():
        if i > 1000000:
            # print('primeFactors', set(primeFactors))
            return primeFactors
        if 1000000 % i == 0:
            k = 1
            while k * i < 1000000:
                primeFactors.append(k*i)
                k += 1

    print('primeFactors ', primeFactors)

def makeFactorsMap():
  fMap = {}
  for pr in primeMap.keys():
    if (pr > 1000000):
        writePrimeFactorsMap(fMap)
        return
    curI = 1
    cur = []
    while pr * curI < 1000000:
        cur.append(pr*curI)
        curI += 1
    fMap[pr] = cur

@track_performance
def makePrimeMapFor2and5To1M():
  primeMap = {}
  curItem = 2
  curI = 1
  cur = []
  while curItem * curI < 100:
      cur.append(curItem*curI)
      curI += 1
  primeMap[curItem] = cur 
  curItem = 5
  curI = 1
  cur = []
  while curItem * curI < 100:
      cur.append(curItem*curI)
      curI += 1
  primeMap[curItem] = cur
  combinedMap = list(set([*primeMap[2], *primeMap[5]]))
  print('combined', combinedMap)


def writePrimeFactorsMap(factorsMap):    
  f = open("./resources/factorsTo1M.txt", "x+")
  json.dump(factorsMap, f)
  f.close()

# oneM()
# makePrimeMapFor2and5To1M()
makeFactorsMap()