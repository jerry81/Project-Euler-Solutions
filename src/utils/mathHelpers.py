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
  for pivot in range(0, limit-1):
    current = initArr[pivot]
    if (current['touched'] == False):
      current['touched'] = True
      current['prime'] = True
    for processed in range(pivot, limit-1):
      current2 = initArr[processed]
      rem = current2['val'] % current['val']
      if rem == 0 and current2['touched'] == False:
        current2['touched'] = True
        current2['prime'] = False 
  filtered = list(filter(lambda x: x['prime'] == True, initArr))
  mapped = list(map(lambda x: x['val'], filtered))
  return mapped 
      
