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
# makeFactorsMap()

def readFactorsMap():
    f = open("./resources/factorsTo1M.txt", 'r')
    asJson = json.load(f)
    # print('last item ', list(asJson.keys())[78497])
    return asJson

def convertFactorsMap():
    f = open("./resources/factorsMapTo1M.txt", 'x+')
    factorsMapOfArr = readFactorsMap()
    returnedMap = {} 
    for key, val in factorsMapOfArr.items():
      curMap = {}
      for v in val:
          curMap[v] = True
      returnedMap[key] = curMap
    json.dump(returnedMap, f)

def makePrimeFactorsMap():
    f = open("./resources/primeFactorsTo1M.txt", 'x+')
    factorsMap = readFactorsMap()
    primes = list(factorsMap.keys())
    primeFactors = {}
    # init the map 
    for i in range(2,1000001):
        primeFactors[i] = []
        if i % 100000 == 0:
            print('currently processing ', i)
        if o1isPrime(i):
            continue
        for pr in primes:
            if int(pr) >= i:
                continue
            if i % int(pr) == 0:
                highestIndex = i // int(pr)
                primeFactors[i] = [*primeFactors[i], *factorsMap[pr][:(highestIndex - 1)]]
        primeFactors[i] = list(set(primeFactors[i]))
    json.dump(primeFactors, f)

# readFactorsMap()
# makePrimeFactorsMap()
convertFactorsMap()