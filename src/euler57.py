from utils.annotations import track_performance
from fractions import Fraction

print('project euler problem 57')

def useDenom(target, num, denom = None):
  if (denom == None):
    return Fraction(num * target, target)
  return Fraction(target * num, target * denom)

def expDenom(cur):
  return Fraction(1) / (Fraction(2) + cur)

def longSqrt(expansions):
  right = Fraction(1, 2)
  for i in range(expansions):
    right = expDenom(right)
  return Fraction(1, 1) + right
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

def testLongSqrt():
  print('3/2 is ', longSqrt(1))
  print('7/5 is ', longSqrt(2))
  for i in range(3, 9):
    print('next iter', longSqrt(i))

@track_performance
def euler57():
  LIMIT = 1001
  count = 0
  for i in range(1, LIMIT):
    nextIter = longSqrt(i)
    if len(str(nextIter.numerator)) > len(str(nextIter.denominator)):
      count += 1
  print(count)

euler57()
testUseDenom()
testExpDenom()
testLongSqrt()