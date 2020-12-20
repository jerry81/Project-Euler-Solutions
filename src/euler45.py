from math import sqrt
print('project euler problem 45')

def getTriangular(input):
  return input * (input + 1) / 2

def isPentagonal(input): 
  result = (1 + sqrt(1 + 24 * input)) / 6
  return int(result) == result

def isHexagonal(input):
  result = (1 + sqrt(1 + (8 * input))) / 4
  return int(result) == result

print(isPentagonal(22))
print(isHexagonal(45))

test1 = getTriangular(285)
print(test1)
print(isPentagonal(test1))
print(isHexagonal(test1))

i = 286
while (True):
  nextTri = getTriangular(i)
  if isPentagonal(nextTri) and isHexagonal(nextTri):
    break
  i += 1
print(i)
print(getTriangular(i))