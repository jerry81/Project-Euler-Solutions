import copy
import itertools

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

def getAllPerms(nextPerm): 
  allItems = [nextPerm]
  while True:
    prev = nextPerm
    nextPerm = getNextPermutation(nextPerm[:])
    if (prev == nextPerm):
      break
    else: 
      allItems.append(nextPerm)
  return allItems

def getPermsOfNumber(num, withMemo = False, memo = {}):
  asList = list(str(num))
  fun = getAllPerms
  seq = list(range(len(asList)))
  if withMemo:
    idxArr, memo = getPermutationsRWithMemo(seq, memo)
  else:
    idxArr = getAllPerms(seq)
  newArr = []
  for a in idxArr:
    newNum = []
    for i in a:
      dig = asList[i]
      newNum.append(dig)
    newArr.append(newNum)
  asInts = list(map(lambda x: int("".join(x)), newArr))
  return asInts, memo

def getPermsOfNumberM(num, memo):
  return getPermsOfNumber(num, True, memo)


def getPermsOfNumberOOTB(num):
  asList = list(str(num))
  return list(
    map(
      lambda x: int("".join(x)), itertools.permutations(asList)
    )
  )

def testOOTB():
  print('OOTB', getPermsOfNumberOOTB(12345))

def getPermutationsR(arr):
  if len(arr) == 1:
    return arr
  if len(arr) == 2:
    rev = copy.copy(arr)
    rev.reverse()
    return [arr, rev]
  # isolate first item 
  sub1 = arr[:1][0]
  sub2 = arr[1:]
  permutations = getPermutationsR(sub2)
  expanded = []
  for i in range(len(arr)):
    for idx, p in enumerate(permutations):
      c = copy.copy(p)
      c.insert(i, sub1)
      expanded.append(c)
  return expanded

def checkMap(num, _map):
  value = _map.get(num, None)
  if value is not None:
    return True
  return False

def getPermutationsRWithMemo(arr, memo):
  if len(arr) == 1:
    return arr
  if len(arr) == 2:
    rev = copy.copy(arr)
    rev.reverse()
    return [arr, rev]
  # isolate first item 
  sub1 = arr[:1][0]
  sub2 = arr[1:]
  sub2C = copy.copy(sub2)
  sub2Key = "".join(list(map(lambda x: str(x), sub2C)))
  if checkMap(sub2Key, memo):
    print('memo used')
    permutations = memo[sub2]
  else:
    permutations = getPermutationsR(sub2)
    memo[sub2Key] = permutations
  expanded = []
  for i in range(len(arr)):
    for idx, p in enumerate(permutations):
      c = copy.copy(p)
      c.insert(i, sub1)
      expanded.append(c)
  return expanded, memo

def testMemo():
  print('1552 is ', getPermsOfNumberM(1552, {}))

def testGetPermutationsR():
  test1 = [1,2]
  test2 = [5,6]
  test3 = [1,2,3]
  test4 = [1,2,3,4]
  print('12 21 is ', getPermutationsR(test1))
  print('56, 65 is ', getPermutationsR(test2))
  print('123, 132, etc... is ', getPermutationsR(test3))
  print('1234, 1243, etc... is ', getPermutationsR(test4))

firstPerm = [1,2,3,4,5,6,7,8,9]

def testPermutations():
  print('permutations are 123 132 213 231 312 321', getAllPerms(list('123')))
  print('permutations are 1234 1243 1324 1342 1423 1432 etc...', getAllPerms(list('1234')))
  seqArr = list(range(5))
  print('permutations are 01234 01243 etc...', getAllPerms(seqArr))

def testGetPermsOfNumber():
  print('permutations are 123 132 213 231 312 321', getPermsOfNumber(123))
  print('permutations are 123 132 213 231 312 321', getPermsOfNumber(321))
  print('permutations are 221 122 212 122 212 etc...', getPermsOfNumber(221))

# testPermutations()
# testGetPermsOfNumber()
# testGetPermutationsR()

# testOOTB()
testMemo()