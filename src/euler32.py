print('project euler problem 32')

import copy

def swap(arr, idx1, idx2):
  arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
  return arr

testBase = [1,2,3,4,5]
testSwap = copy.copy(testBase)
res = swap(testSwap, 0,4)
testReverse = copy.copy(testBase)
reverseRes = testReverse[::-1]
testSlice = testBase[:]
sliced = testBase[2:4]
joined = testBase[0:2] + testBase[2:5]
print('reverseRes is ', reverseRes)
print('sliced is ', sliced)
print('joined is ', joined)
print('testBase is ', testBase)
