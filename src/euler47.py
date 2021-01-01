from math import sqrt
from utils.mathHelpers import isPrime
print('project euler problem 47')

def getFactors(input): 
  factors = []
  for i in range(1, int(sqrt(input)+1)):
    if input % i == 0:
      factors.append(i)
      factors.append(int(input/i))
  return list(filter(lambda x: x != 1 and isPrime(x), factors))


print('14', getFactors(14))
print('15', getFactors(15))

print('644', getFactors(644))
print('645', getFactors(645))
print('646', getFactors(646))
print('134043', getFactors(134043))
print('134044', getFactors(134044))
print('134045', getFactors(134045))
print('134046', getFactors(134046))
print('238203', getFactors(238203))
print('238204', getFactors(238204))
print('238205', getFactors(238205))
print('238206', getFactors(238206))

streak = 0
cur = 100000
while streak < 4:
  print('cur is ', cur)
  if len(getFactors(cur)) == 4:
    print('getfactors', getFactors(cur))
    print('len is ', len(getFactors(cur)))
    streak += 1
  else:
    streak = 0
  cur+=1

print('final cur is ', cur)