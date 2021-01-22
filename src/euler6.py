print('project euler problem 6')

def squareOfSums(num):
  total = 0
  for i in range(1, num+1):
    total += i
  return total**2

def sumOfSquares(num):
  total = 0
  for i in range(1, num+1):
    total += i**2
  return total

print(sumOfSquares(100) - squareOfSums(100))