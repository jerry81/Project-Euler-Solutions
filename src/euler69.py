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


@track_performance
def euler69():
    print('project euler problem 69')
    for i in range(2, 1000000):
        getFactors(i)


def testFactors():
    print('factors without 1 27', getFactorsWithout1(27))
    print('factors without 1 42', getFactorsWithout1(42))
    print('factors without 1 42', getFactorsWithout1(42))


def testRp():
    for i in range(2, 11):
        print('testRP i is ', i, getRelativePrimes2(i))


# euler69()
# testFactors()
testRp()
