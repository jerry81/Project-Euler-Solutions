import math

def isPandigital(inputN):
  asStr = str(inputN)
  if len(asStr) != 9:
    return False
  panSet = set("123456789")
  return len(panSet.intersection(set(asStr))) == 9

def longDivision(divisor, dividend):
    quotientArr = []
    repeatArr = []
    while (True): 
      quotient = dividend // divisor
      quotientArr.append(quotient)
      remainder = dividend % divisor
      if (repeatArr.count(remainder) > 0):
        break
      if remainder == 0:
        break
      else:
        repeatArr.append(remainder)
        dividend = remainder * 10
    return quotientArr


def isPrime(input):
  if input == 0:
    return False
  if input == 1: 
    return False
  if input < 0:
    return False
  for x in range(2, (int)(math.sqrt(input))+1):
    if ((input % x) == 0):
      return False
  return True

def reduceFraction(fraction):
  numerator = fraction[0]
  denom = fraction[1]
  maxDiv = min(numerator, math.floor(denom / 2))
  for div in range(maxDiv, 0, -1):
    rem = numerator % div 
    rem2 = denom % div
    if rem == 0 and rem2 == 0:
      return (numerator//div, denom//div)
  return (numerator, denom)

def eratosthenes(limit):
  initArr = []
  for i in range(2, limit+1):
    initArr.append({ "val": i, "prime": False, "touched": False })
  # setup done 
  print('setup done')
  for pivot in range(0, limit-1):
    current = initArr[pivot]
    if (current['touched'] == False):
      current['touched'] = True
      current['prime'] = True
    start = current['val']**2
    while start < limit:
      current2 = initArr[start-2]
      current2['touched'] = True
      current2['prime'] = False 
      start += current['val']
  filtered = list(filter(lambda x: x['prime'] == True, initArr))
  mapped = list(map(lambda x: x['val'], filtered))
  return mapped 
      
def getFactors(number):
  returned = []
  for i in range(1, int(math.sqrt(number)) + 1):
    if number%i == 0:
      returned.append(i)
      returned.append(number // i)
  return returned
  

def getXTriangles(x):
  triangles = []
  for i in range(0, x):
    num = i + 1
    triangles.append((num * (num +1)) // 2)
  return triangles

def getNextLexicalPermutation(current):
        for i in range(len(current) - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                        compared = current[j]
                        for k in range(i, j-1, -1):
                            pivot = current[k]
                            if compared < pivot:
                                    current[k] = compared
                                    current[j] = pivot 
                                    sublist = current[j+1:]
                                    sublist.reverse()
                                    current[j+1:] = sublist
                                    return current
        current.reverse()
        return current

def fib(termIdx):
  if termIdx == 0:
    return 1
  if termIdx == 1:
    return 2
  return fib(termIdx - 1) + fib(termIdx - 2)

def eratosthenesWithSupport(fname, start, limit):
  f = open(fname, "r")
  asStr = f.read()
  asList = asStr.split(',')
  initArr = []
  for i in range(2, limit+1):
    initArr.append({ "val": i, "prime": False, "touched": False })
  for j in range(0, len(asList)):
    prime = int(asList[j])
    initArr[prime-2]['prime'] = True
    initArr[prime-2]['touched'] = True
  # setup done 
  print('setup done')
  for pivot in range(start, limit-1):
    current = initArr[pivot]
    if (current['touched'] == False):
      current['touched'] = True
      current['prime'] = True
    start = current['val']**2
    while start < limit:
      current2 = initArr[start-2]
      current2['touched'] = True
      current2['prime'] = False 
      start += current['val']
  filtered = list(filter(lambda x: x['prime'] == True, initArr))
  mapped = list(map(lambda x: x['val'], filtered))
  return mapped 

def testGetAllFactors():
  print('get all factors 15 ', getFactors(15))
  print('get all factors 42 ', getFactors(42))

# testGetAllFactors()
