from utils.annotations import track_performance
from fractions import Fraction

print('project euler problem 57')

def useDenom(target, num, denom = None):
  if (denom == None):
    return Fraction(num * target, target)
  return Fraction(target * num, target * denom)

def expDenom(cur):
  return Fraction(1) / (Fraction(2) + cur)

def longSqrt(base, expansions):
  pass
  # expansions = 4
  # 1 / (2 + (1 / (2 + (1 / (2 + (1 / 2))

def testUseDenom():
  fraction1 = useDenom(2, 18, 36)
  fraction2 = useDenom(2, 2)
  print('1/2 is ', fraction1)
  print('4/2 is ', fraction2)
  pro = fraction1*fraction2
  print('4/4 is ', pro)

def testExpDenom():
  first = expDenom(Fraction(1, 2))
  second = expDenom(first)
  third = expDenom(second)
  print('2/5 is ', first)
  print('5/12 is ', second)
  print('12/29 is ', third)

@track_performance
def euler57():
  print('57')

euler57()
testUseDenom()
testExpDenom()