from math import sqrt
from utils.mathHelpers import isPrime
print('project euler problem 46')
print(isPrime(33))

composites = []
primes = []
doubleOfSquares = []
for i in range(4, 4000):
  nextOdd = (2 * i) + 1
  if (not isPrime(nextOdd)):
    composites.append(nextOdd)

for i in range(0, 4000):
  nextOdd = (2 * i) + 1
  if (isPrime(nextOdd)):
    primes.append(nextOdd)

for i in range(0, 100):
  nextItem = 2 * (i ** 2)
  doubleOfSquares.append(nextItem)

print("composites is ", composites)
print("primes is ", primes)
print("double of squares", doubleOfSquares)

def isBuildable(input):
  result = False
  for i in range(0, len(primes)):
    prime = primes[i]
    diff = input - prime
    if (diff in doubleOfSquares):
      result = True
      break
    if (prime > input):
      break
  return result

buildableComposites = []
for i in range(0, len(composites)):
  nextComposite = composites[i]
  print("next composite", nextComposite)
  izBuildable = isBuildable(nextComposite)
  if (not izBuildable):
    print('is buildable', isBuildable(nextComposite))
    buildableComposites.append(nextComposite)
  
  print('buildables are ', buildableComposites)
