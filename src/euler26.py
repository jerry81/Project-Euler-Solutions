print('project euler problem 26')

def longDivision(divisor, dividend):
    quotientArr = []
    repeatArr = []
    while (True): 
      quotient = dividend // divisor
      print("dividend is {} and divisor is {}".format(dividend, divisor))
      print("quotient is {}".format(quotient))
      quotientArr.append(quotient)
      remainder = dividend % divisor
      if (repeatArr.count(remainder) > 0):
        print("repeated and is {}".format(repeatArr))
        break
      print("remainder is {}".format(remainder))
      if remainder == 0:
        break
      else:
        repeatArr.append(remainder)
        dividend = remainder * 10
    return quotientArr

for denominator in range(2, 11): #range second arg is not inclusive
  fraction = 1/denominator
  print("denominator: {} fraction: {}".format(denominator, fraction))
  print("longDivision(({}, 1) is {}".format(denominator, longDivision(denominator, 1)))
