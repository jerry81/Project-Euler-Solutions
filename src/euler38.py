print('project euler problem 38')
from utils.mathHelpers import isPandigital

# min n 2
# max x = 987654321/2
# max n = 9

# formula 

def applyFormula(x, n):
  sumR = ""
  for i in range(1, n+1):
    sumR += str(x*i)
  return sumR

print("9, 5", applyFormula(9, 5))

maxX = 987654321 // 3
for x in range (2, maxX):
  for n in range (2, 5):
    sumR = applyFormula(x, n)
    if isPandigital(sumR):
      print("pan {} {} {}".format(x, n, sumR))

# tests 


