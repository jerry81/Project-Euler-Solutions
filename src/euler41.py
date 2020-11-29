print('project euler problem 41')

from utils.mathHelpers import isPandigital, isPrime
from euler32 import getAllPerms, stringifyAndJoin

allPerms = [stringifyAndJoin(i) for i in getAllPerms([1,2,3,4,5,6,7])]
for cand in range(0, len(allPerms)):
  print('is prime', isPrime(allPerms[cand]))
filtered = [j for j in allPerms if isPrime(j) == True]
print('filtered is ', filtered)

