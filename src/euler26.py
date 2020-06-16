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

longest = []
longestIndex = 2
for denominator in range(2, 1001): #range second arg is not inclusive
  fraction = 1/denominator
  cur = longDivision(denominator, 1) 
  if (len(cur) > len(longest)):
    longest = cur
    longestIndex = denominator
  print("denominator: {} fraction: {}".format(denominator, fraction))
  print("longDivision(({}, 1) is {}".format(denominator, longDivision(denominator, 1)))
print("longest: {} longestIndex: {}".format(longest, longestIndex))
