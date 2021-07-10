from utils.annotations import track_performance
import itertools

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

def getAddendsR(s):
    if s == 2:
        return [[1,1]]
    combos = []
    for i in range(1, s):
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
    return removeDups([*cur, *combos])

def testGetAddendsR():
    print('getAddends 2', getAddendsR(2))
    print('getAddends 3', getAddendsR(3))
    for i in range(4, 12):
        print('getAddends i, and len is ', i, getAddendsR(i), len(getAddendsR(i)))
    """   for i in range(4, 75):
        print('len for i is ', i, len(getAddendsR(i))) """
    # print('getAddends 100 is', getAddendsR(100)[:-200])

def removeDups(k):
      return list(k for k,_ in itertools.groupby(k))

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

# euler76()
testGetAddendsR()
# euler76()