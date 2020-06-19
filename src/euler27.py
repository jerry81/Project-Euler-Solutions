print('project euler problem 27')


from utils.mathHelpers import isPrime

print('isPrime(7) is {}'.format(isPrime(7)))
print('isPrime(8) is {}'.format(isPrime(8)))
print('isPrime(10) is {}'.format(isPrime(10)))
print('isPrime(11) is {}'.format(isPrime(11)))

def quadratic(n, a, b):
  return n**2 + n*a + b


def consecutivePrimes(a, b):
  n = 0
  while (True):
    quadradicResult = quadratic(n,a,b)
    if isPrime(quadradicResult) == False:
      return n
    n += 1

longestStreak = 0
longesta = -1000
longestb = -1000
for a in range(-1000, 1001):
  for b in range(-1000, 1001):
    cur = consecutivePrimes(a, b)
    if (cur > longestStreak):
      longestStreak = cur
      longesta = a
      longestb = b
print('longestStreak a and b {} {} {}'.format(longestStreak, longesta, longestb))