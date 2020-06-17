print('project euler problem 26')
from utils.math import longDivision

longest = []
longestIndex = 2
for denominator in range(2, 1001): #range second arg is not inclusive
  fraction = 1/denominator
  cur = longDivision(denominator, 1) 
  if (len(cur) > len(longest)):
    longest = cur
    longestIndex = denominator
print("longest: {} longestIndex: {}".format(longest, longestIndex))
