print('project euler problem 36')

import math
from utils.mathHelpers import isPrime

def isPalindrome(asStr): 
    for idx in range(0, len(asStr)):
      # compare first and last 
      first = idx
      last = len(asStr) - idx - 1
      if first >= last:
          return True
      firstVal = asStr[first]
      lastVal = asStr[last]
      if firstVal != lastVal:
          return False

def convertToString(input):
    asStr = str(input)
    if asStr[0] == "0" and asStr[1] == "b":
        return asStr[2:]
    else: 
        return asStr

test1 = 525
test2 = 225
test3 = 1221
test4 = 1234

palindromes = []

for idx in range(1, 1000000):
  isIntPalindrome = isPalindrome(convertToString(idx))
  isBinPalindrome = isPalindrome(convertToString(bin(idx)))
  if (isIntPalindrome == True and isBinPalindrome == True):
      palindromes.append(idx)

print("palindromes is ", palindromes)
print("sum is ", sum(palindromes))
"""
print("test1", isPalindrome(convertToString(test1)))
print("test2", isPalindrome(convertToString(test2)))
print("test3", isPalindrome(convertToString(test3)))
print("test4", isPalindrome(convertToString(test4)))

print("bin1", bin(test1))
print("bin to str", convertToString(bin(test1)))
"""