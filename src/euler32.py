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
  for pivot in range(len(ret) - 2, -1, -1):
    pivotValue = ret[pivot]
    for i in range(len(ret) - 1, pivot, -1):
      cur = ret[i]
      if pivotValue < cur:
        ret = swap(ret[:], i, pivot)
        ret = reverseSlice(ret[:], pivot + 1, len(ret))
        return ret
  return ret

testBase = [1,2,3,4,5]
testSwap = copy.copy(testBase)
res = swap(testSwap, 0,4)
testReverse = copy.copy(testBase)
reverseRes = testReverse[::-1]
testSlice = testBase[:]
sliced = testBase[2:4]
joined = testBase[0:2] + testBase[2:5]


nextPerm = [1,2,3,4,5,6,7,8,9]
allPerms = [nextPerm]
while True:
  prev = nextPerm
  nextPerm = getNextPermutation(nextPerm[:])
  if (prev == nextPerm):
    break
  else: 
    allPerms.append(nextPerm)

def stringifyAndJoin(arr):
  s = [str(i) for i in arr]
  return int("".join(s))

print('strngifyandjoin [1,2,3]', stringifyAndJoin([1,2,3]))

# for x in range(0, len(allPerms)):
  # try [0:1]*[1:5] = [5:10]



print('all perms has {} items'.format(len(allPerms)))
