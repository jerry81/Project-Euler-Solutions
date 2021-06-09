from filterArrayAndOutput import primeMap

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

def getNonPrimeOddsToN(n):
    newMap = {}
    for i in range(1, (n//2) + 1):
        j = i * 2 + 1
        if not o1isPrime(j) and j <= n:
            newMap[j] = True
    return newMap

def testNonPrimeOdds():
    print('nonprime odds up to 10M count is ', len(getNonPrimeOddsToN(10000000)))

def diagnoseTotients():
    for i in range(200,400):
        print('totient i is ', i, totient(i))

# testNonPrimeOdds()
# diagnoseTotients()