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