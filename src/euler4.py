print('project euler problem 4')

from utils.stringHelpers import isPalindrome

palis = []
for i in range(1, 1000):
  for j in range(1, 1000):
    if (isPalindrome(str(i*j))):
      palis.append(i*j)

print('max is ', max(palis))