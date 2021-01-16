print('project euler problem 3')

from utils.mathHelpers import isPrime
from math import sqrt

lim = 600851475143

sqlimit = sqrt(lim)

factors = []
for i in range(1, int(sqlimit)):
  if lim % i == 0 and isPrime(i):
    factors.append(i)
  
print(factors)