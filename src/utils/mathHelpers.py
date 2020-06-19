import math

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