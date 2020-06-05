print('project euler problem 26')
print ('1%2 is ', 1%2)

def longDivision(divisor, dividend):
    quotientArr = []
    repeatArr = []
    while (True): 
      quotient = dividend // divisor
      print('quotient is {}', quotient)
      quotientArr.append(quotient)
      remainder = dividend % divisor
      print('remainder is {}', remainder)
      if remainder == 0:
        break
      else:
        dividend *= 10
    return quotientArr

for denominator in range(2, 11): #range second arg is not inclusive
  fraction = 1/denominator
  print("denominator: {} fraction: {}".format(denominator, fraction))
  print("longDivision(({}, 1) is {}".format(denominator, longDivision(denominator, 1)))
