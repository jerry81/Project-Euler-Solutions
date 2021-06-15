from filterArrayAndOutput import primeMap
from myitertools import getFingerprint

def arePerms(a,b):
    return getFingerprint(int(a)) == getFingerprint(int(b))

primeList = list(primeMap.keys())

def o1isPrime(n):
    try:
        prime = primeMap[n]
        return True
    except:
        return False


def totient(x):
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

# euclidean algorithm
def getGCD(a,b):
    while b!=0:
        c = a % b
        a = b
        b = c
    return a

# def totient2(x):


def getNonPrimeOddsToN(n, minimum = 0):
    newMap = {}
    for i in range(1, (n//2) + 1):
        j = i * 2 + 1
        if not o1isPrime(j) and j <= n:
            if j >= minimum:
              newMap[j] = True
    return newMap

def testNonPrimeOdds():
    print('nonprime odds up to 10M count is ', len(getNonPrimeOddsToN(10000000)))

def diagnoseTotients():
    for i in range(200,400):
        print('totient i is ', i, totient(i))

def getPrimesBetween(a,b):
    output={}
    for key,val in primeMap.items():
        if int(key) > a and int(key) < b:
            output[key] = val
    return output

def testGetPrimesBetween():
    print('getPrimesBetween test ', getPrimesBetween(3000, 5000))

def totientOfSubprimes(a,b):
    return (a-1)*(b-1)

def makePairStr(a,b):
    return str(a) + ',' + str(b)

def getCandidates():
    primes = getPrimesBetween(2000, 5000)
    properPermsUnder10M = []
    for k,v in primes.items():
        for k2,v2 in primes.items():
          prod = k * k2 
          if prod > 10000000:
              continue
          totient = totientOfSubprimes(k, k2)
          if not arePerms(totient, prod):
              continue
          properPermsUnder10M.append(prod)
    return properPermsUnder10M
                  
    
def testMakePairStr():
    print('make pair 5, 10', makePairStr(5,10))
    print('make pair 7, 11', makePairStr(7,11))

def getPairFromKey(s):
    x = s.split(',')
    print('x is', x)

def testGetPair():
    print('from 5,10', getPairFromKey('5,10'))

# testNonPrimeOdds()
# diagnoseTotients()
# testGetPrimesBetween()
print('candidates are ', getCandidates())
# testMakePairStr()
# testGetPair()