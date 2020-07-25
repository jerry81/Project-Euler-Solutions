print('project euler problem 32')

import copy

def swap(arr, idx1, idx2):
  arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
  return arr

def reverseSlice(arr, idx1, idx2):
  sliced = arr[idx1:idx2+1]
  prefix = arr[0:idx1]
  reversedSlice = sliced[::-1]
  return prefix + reversedSlice

def getNextPermutation(input):
  ret = input[:]
  for i in range(len(ret) - 1, -1, -1):
    cur = ret[i]
    print('cur is ', cur)
    for j in range(i - 1, -1, -1):
      comp = ret[j]
      if j < i:
        ret = swap(ret[:], i, j)

  return ret

testBase = [1,2,3,4,5]
testSwap = copy.copy(testBase)
res = swap(testSwap, 0,4)
testReverse = copy.copy(testBase)
reverseRes = testReverse[::-1]
testSlice = testBase[:]
sliced = testBase[2:4]
joined = testBase[0:2] + testBase[2:5]


testPerm = [1,2,3,4,5]
reversedSlice = reverseSlice(testPerm[:], 3, 4)
nextPerm = getNextPermutation(testPerm)
print('nextPerm is ', nextPerm)
print('reverseSlice is ', reversedSlice)