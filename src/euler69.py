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
    return rps

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

def getStats(n, rps):
    count = len(rps)
    return n / count


@track_performance
def euler69():
    print('project euler problem 69')
    tmax = (11550, 4.1825)
    for i in range(20000, 100000):
        cur = getStats(i, getRP(i))
        a, b = tmax
        if cur > b:
            tmax = i, cur
    print('tmax is ', tmax)


def testFactors():
    print('factors without 1 27', getFactorsWithout1(27))
    print('factors without 1 42', getFactorsWithout1(42))
    print('factors without 1 42', getFactorsWithout1(42))


def testRp():
    for i in range(2, 11):
        print('getRp i is ', i, getRP(i))


euler69()
# testFactors()
# testRp()
