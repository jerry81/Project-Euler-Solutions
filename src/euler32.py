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

summed = 0
products = set()
for x in range(0, len(allPerms)):
  # = [5:10]
  perm = allPerms[x]
  product = stringifyAndJoin(perm[5:10])
  
  # try [0:1]*[1:5]
  operand1 = stringifyAndJoin(perm[0:1])
  operand2 = stringifyAndJoin(perm[1:5])
  triedProduct = operand1 * operand2
  if triedProduct == product:
    print('hit', product, operand1, operand2)
    products.add(product)

  # try [0:2] * [2:5]
  operand3 = stringifyAndJoin(perm[0:2])
  operand4 = stringifyAndJoin(perm[2:5])
  triedProduct2 = operand3 * operand4
  if triedProduct2 == product:
    print('hit', triedProduct2, operand3, operand4)
    products.add(product)

for prod in products:
  summed += prod

print('all perms has {} items'.format(len(allPerms)))
print('summed is ', summed)