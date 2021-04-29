from utils.annotations import track_performance
from fractions import Fraction

print('project euler problem 57')

def useDenom(target, num, denom = None):
  if (denom == None):
    return Fraction(num * target, target)
  return Fraction(target * num, target * denom)

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

@track_performance
def euler57():
  print('57')

euler57()
testUseDenom()