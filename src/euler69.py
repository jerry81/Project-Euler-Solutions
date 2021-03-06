from utils.annotations import track_performance
from utils.mathHelpers import getFactors, isPrime
from filterArrayAndOutput import primeMap

factorsMap = {}
primeList = list(primeMap.keys())


def getFactorsWithout1(n):
    try:
        f = factorsMap[n]
        return f
    except:
        factors = getFactors(n)
        factors.pop(0)
        factorsMap[n] = factors
        return factors


def hasCommon(a, b):
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
    for i in range(1, n):
        factorsOfI = getFactorsWithout1(i)
        if not hasCommon(factorsOfI, factorsOfN):
            rp.append(i)
    return rp


def getRelativePrimes2(n):
    rps = [1]
    seive = {}
    for i in range(2, n):
        # check seive first
        try:
            cur = seive[i]
            continue
        except:
            divisible = n % i == 0
            seive[i] = divisible
            for j in range(i, n//i):
                cur = i*j
                try:
                    s = seive[cur]
                except:
                    seive[cur] = divisible
    for (key, val) in seive.items():
        if not val:
            rps.append(key)
    return rps


def processSeive(seive):
    rps = [1]
    for (key, val) in seive.items():
      if val:
          rps.append(key)
    rps.sort()
    return rps

def o1isPrime(n):
    try:
        prime = primeMap[n]
        return True
    except:
        return False

def getRP(n):
    seive = {}
    primes = primeMap.keys()
    if n in primes:
        return list(range(1, n))
    while True:
        for pr in primes:
            if pr >= n:
                return processSeive(seive)
            nonfactor = n%pr != 0 # nonfactor true means it is coprime
            seive[pr] = nonfactor
            for i in range(2, n//pr + 1):
                j = i * pr
                if j < n:
                    try:
                        se = seive[j]
                        if not se or nonfactor:
                            continue
                        seive[j] = nonfactor
                    except:
                        seive[j] = nonfactor
    return processSeive(seive)

coprimeMap = {}

def prepareCoprimeMap(lim):
    for i in primeMap.keys():
        if i > lim:
            return coprimeMap
        curCoprimeMap = {}
        for j in range(1, lim//i + 1):
            k = i * j
            curCoprimeMap[k] = False
        coprimeMap[i] = curCoprimeMap
    return coprimeMap

def prepareCoprimeMapNoEvens(lim):
    for i in primeMap.keys():
        if i > lim:
            return coprimeMap
        curCoprimeMap = {}
        if i == 2:
            for j in range(1, lim//i + 1):
              k = i * j
              curCoprimeMap[k] = False
        else: 
            for j in range(1, ((lim//i) // 2) + 2):
                k = i * ((j * 2) -1)
                if k > lim:
                    continue
                curCoprimeMap[k] = False
        coprimeMap[i] = curCoprimeMap
    return coprimeMap

def getRP2(n):
    if o1isPrime(n):
        return n-1
    primes = primeMap.keys()
    tcoprimes = {}
    for pr in primes:
        isNotCoprime = n % pr == 0
        if pr > n:
            return n - len(tcoprimes.keys())
        if isNotCoprime:
            if pr != n:
                tcoprimes[pr] = False
            sliced = sliceToX(pr,n)
            tcoprimes = {**tcoprimes, **sliced}
 
def getRP3(n):
    if o1isPrime(n):
        return n-1
    primes = primeMap.keys()
    tcoprimes = {}
    for pr in primes:
        isNotCoprime = n % pr == 0
        if pr > n:
            return n - len(tcoprimes.keys())
        if isNotCoprime:
            if pr != n:
                tcoprimes[pr] = False
            sliced = sliceToX2(pr,n)
            tcoprimes = {**tcoprimes, **sliced}
 

def getStats(n, rps):
    count = len(rps)
    return n / count

@track_performance
def euler69():
    print('project euler problem 69')
    # prepareCoprimeMapNoEvens(1000000)
    # print('done preparing')
    tmax = 0,0
    for i in range(1, 500000):
        x = i*2
            
        cur = x/toilent(x)
        a, b = tmax
        if cur > b:
            tmax = x, cur
    print('tmax is ', tmax)

def testPrepareCoprimeMap():
    prepareCoprimeMap(11)
    print('coprime map up to x is ', coprimeMap)
    print('testing merging coprime map 2 and 3')
    newCPM = {**coprimeMap[2], **coprimeMap[3]}
    print('newCPM is ', newCPM)

def testPrepareCoprimeMapNE():
    prepareCoprimeMapNoEvens(25)
    print('coprime map up to x is ', coprimeMap)
    print('testing merging coprime map 2 and 3')
    newCPM = {**coprimeMap[2], **coprimeMap[3]}
    print('newCPM is ', newCPM)

def testPreparePerf():
    print('testing perf of coprime map (no output)')
    prepareCoprimeMap(1000001)
    print(coprimeMap)

def sliceToX(cp, x):
    cpm = list(coprimeMap[cp].items())
    itemsNeeded = (x // cp) 
    while True:
        item, _ = cpm[itemsNeeded]
        if (item >= x):
            break
        itemsNeeded +=1
    return dict(cpm[:itemsNeeded])

# used with coprimes without evens
def sliceToX2(cp, x):
    cpm = list(coprimeMap[cp].items())
    itemsNeeded = (x // cp) // 2
    if cp == 2:
        itemsNeeded = (x // cp) 
    while True:
        item, _ = cpm[itemsNeeded]
        if (item >= x):
            break
        itemsNeeded +=1
    return dict(cpm[:itemsNeeded])

def slicePrimesToX(x):
    floor10 = (x // 10) + 1
    minIndex = 4 * floor10
    print('min index is ', minIndex)
    pm = list(primeMap.items())
    primes = list(primeMap.keys())
    n = 1
    while True:
      if n > x:
          return dict(pm[:minIndex])
      n = primes[minIndex]
      print('n is now ', n)
      minIndex-=1   

def toilent(x):
    num = 1
    denom = 1
    if o1isPrime(x):
      return x - 1
    for i in primeList:
      if i > x:
          return (x * num)/denom
      if x % i == 0:
          denom *= i
          num *= i-1

def testSliceCoprimeMap():
    prepareCoprimeMap(100)
    print('fullCPM to 100 for item 2 is ', coprimeMap[2])
    print('sliceToX 2, 10 is', sliceToX(2, 10))
    print('slice to x 3, 10 is ', sliceToX(3, 10))

def testFactors():
    print('factors without 1 27', getFactorsWithout1(27))
    print('factors without 1 42', getFactorsWithout1(42))
    print('factors without 1 42', getFactorsWithout1(42))


def testRp():
    prepareCoprimeMap(1000000)
    print('getRp 11 is ', getRP2(11))
    print('getRp 12 is ', getRP2(12))
    print('getRp 13 is ', getRP2(13))
    print('getRp 14 is ', getRP2(14))
    print('getRp 15 is ', getRP2(15))
    print('getRp 16 is ', getRP2(16))
    print('getRp 18 is ', getRP2(18))
    print('getRp 19 is ', getRP2(19))
    print('getRp 20 is ', getRP2(20))    
    """     for i in range(2, 12):
        print('getRp i is ', i, getRP2(i)) """



def testRP2():
    prepareCoprimeMapNoEvens(1000000)
    print('getRp30030 is, ', getRP3(30030))

def testSlicePrimes():
    print('to 100 are ', slicePrimesToX(100))

def testToilent():
    for i in range(2,12):
      print('toilent i is ', i, toilent(i))
    print('toilent i is ', 20000, toilent(20000))
    print('toilent i is ', 49998, toilent(49998))
euler69()

# testFactors()
# testRp()
# testPrepareCoprimeMap()
# testSliceCoprimeMap()
# testPreparePerf()
# testPrepareCoprimeMapNE()
# testRP2()
# testSlicePrimes()
# testToilent()