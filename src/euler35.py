print('project euler problem 35')

import math
from utils.mathHelpers import isPrime

def getNextRotation(input): 
    asStr = str(input)
    newString = ''
    for idx in range(0, len(asStr)-1):
      newString += asStr[idx+1]
    newString += asStr[0]
    return newString

def getRotations(input):
    asStr = str(input)
    rotations = []
    rotations.append(int(asStr))
    for _ in range(0, len(asStr)-1):
        asStr = getNextRotation(asStr)
        rotations.append(int(asStr))
    return rotations

primes = []
for cur in range (0, 1000000):
  rots = getRotations(cur)
  prime = True
  for i in range (0, len(rots)):
      if isPrime(rots[i]) != True:
          prime = False
  
  if (prime):
      primes.append(cur)
      print("prime for {} is {}".format(cur, prime))

print("primes is ", len(primes))
        