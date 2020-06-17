print('project euler problem 26')


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

longest = []
longestIndex = 2
for denominator in range(2, 1001): #range second arg is not inclusive
  fraction = 1/denominator
  cur = longDivision(denominator, 1) 
  if (len(cur) > len(longest)):
    longest = cur
    longestIndex = denominator
print("longest: {} longestIndex: {}".format(longest, longestIndex))
