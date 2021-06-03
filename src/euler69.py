from utils.annotations import track_performance
from utils.mathHelpers import getFactors, isPrime
from filterArrayAndOutput import primeMap

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

def getRP2(n):
    coprimeMap = prepareCoprimeMap(n)
    if o1isPrime(n):
        return n-1
    isEven = n % 2 == 0
    cfactors = {} # common factors
    primes = primeMap.keys()
    for pr in primes:
        isCoprime = n % pr != 0
        if pr > n:
            print('cfactors ', cfactors)
            return n - len(cfactors.keys())
        if isCoprime:
            cfactors = {**cfactors, **coprimeMap[pr]}
    return cfactors


def getStats(n, rps):
    count = len(rps)
    return n / count

@track_performance
def euler69():
    print('project euler problem 69')
    prepareCoprimeMap(1000000)
    tmax = (11550, 4.1825)
    for i in range(20000, 1000000):
        cur = getRP2(i) / i
        a, b = tmax
        if cur > b:
            tmax = i, cur
    print('tmax is ', tmax)

def testPrepareCoprimeMap():
    prepareCoprimeMap(11)
    print('coprime map up to 11 is ', coprimeMap)
    print('testing merging coprime map 2 and 3')
    newCPM = {**coprimeMap[2], **coprimeMap[3]}
    print('newCPM is ', newCPM)

def testPreparePerf():
    print('testing perf of coprime map (no output)')
    prepareCoprimeMap(1000001)
    print(coprimeMap)

def sliceToX(cp, x):
    cpm = list(coprimeMap[cp].items())
    itemsNeeded = x // cp 
    return dict(cpm[:itemsNeeded])

def testSliceCoprimeMap():
    prepareCoprimeMap(100)
    print('fullCPM to 100 for item 2 is ', coprimeMap[2])
    print('sliceToX 2, 10 is', sliceToX(2, 10))

def testFactors():
    print('factors without 1 27', getFactorsWithout1(27))
    print('factors without 1 42', getFactorsWithout1(42))
    print('factors without 1 42', getFactorsWithout1(42))


def testRp():
    for i in range(2, 36):
        print('getRp i is ', i, getRP2(i))


# euler69()
# testFactors()
# testRp()
# testPrepareCoprimeMap()
testSliceCoprimeMap()
# testPreparePerf()