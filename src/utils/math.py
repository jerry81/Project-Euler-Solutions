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

def hasDivisors