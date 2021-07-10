from utils.annotations import track_performance
import itertools
from utils.memoHelper import inMap

# sums of 5
# 1,4
# 2,3
# 1, sums of 4 - 1,3,1
  # 1,2,2
  # 1,2,1,1 
  # 1,1,1,1,1
# 2, sums of 3 - 2,1,1,1  - repeat
     # 2, 2, 1 - repeats with sums of 4
# 3, sums of 2 - 3,1,1 - repeats with sums of 4

# sums of 4
# 1, sums of 3 - 1,1,1
   # 1,1,2
# 2, sums of 2
  # 2, 1, 1 - repeat with sums of 3
# 3, 1
# 2, 2

# sums of 3
# 1, sums of 2 - 1,1,1
# 2, 1 

# sums of 2
# 1,1

# sum 7

# 1,1...1
# 2,5
# 2,2,3
# 3,3,1

def removeDups(k):
      k.sort()
      return list(k for k,_ in itertools.groupby(k))

memo = {}

def getAddendsR(s):
    if s == 2:
        return [[1,1]]
    combos = []
    for i in range(1, s):
      prev = None
      if inMap(s-i, memo):
          prev = memo[s-i]
      else:
          prev = getAddendsR(s-i)
      # TODO: memoize
      processedPrev = list(map(lambda arr: [i, *arr], prev))
      for pp in processedPrev:
          pp.sort()
      combos = [*combos, *processedPrev]
    # process the two item breakdowns
    cur = []
    for i in range(1, s//2 + 1):
      cur.append([i, s-i])
    combined = [*cur, *combos]
    asSet = removeDups(combined)
    memo[s] = asSet
    return asSet

def testGetAddendsR():
    print('getAddends 2', getAddendsR(2))
    print('getAddends 3', getAddendsR(3))
    for i in range(4, 12):
        print('getAddends i, and len is ', i, getAddendsR(i), len(getAddendsR(i)))
    for i in range(4, 25):
        print('len for i is ', i, len(getAddendsR(i))) 
    # print('getAddends 100 is', getAddendsR(100)[:-200])

@track_performance
def euler76():
    print('project euler problem 76')
    # print(len(getAddendsR(100)))
    # try removing dups
    permsOf100 = getAddendsR(100)
    for i in permsOf100:
        i.sort()
    filtered = list(permsOf100 for permsOf100,_ in itertools.groupby(permsOf100))
    print('len is ', len(filtered))

def testRemoveDups():
    print('removeDups test 1', removeDups([[1,2], [1,2]]))
    print('removeDups test 2', removeDups([[1, 5], [2, 4], [3, 3], [1, 1, 4], [1, 2, 3], [1, 1, 1, 3], [1, 1, 2, 2], [1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 1, 1, 1, 2], [1, 1, 1, 3], [1, 2, 3], [2, 2, 2], [1, 1, 2, 2], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 3], [1, 1, 1, 3], [1, 1, 4]]))

# euler76()
testGetAddendsR()
# euler76()
# testRemoveDups()