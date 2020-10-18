print('project euler problem 37')

import math
from utils.mathHelpers import isPrime

def getIterations(asStr): 
    iterations = set()
    for idx in range(0, len(asStr)):
      # compare first and last 
      subStr = asStr[idx:len(asStr)]
      subStr2 = asStr[0:idx+1]
      iterations.add(int(subStr))
      iterations.add(int(subStr2))
    return iterations

passed = []

for idx in range(10, 1000000):
  iter = getIterations(str(idx))
  passes = True
  for item in iter:
    if (not(isPrime(item))):
        passes = False
        break
  if (passes):
      passed.append(idx)

print('passed is ', passed)
print('sum is ', sum(passed))

