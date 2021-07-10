from utils.annotations import track_performance

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

def getAddendsR(s):
    if s == 2:
        return [[1,1]]
    prev = getAddendsR(s-1)
    # TODO: memoize
    processedPrev = list(map(lambda arr: [1, *arr], prev))
    # process the two item breakdowns
    cur = []
    for i in range(1, s//2 + 1):
      cur.append([i, s-i])
    return [*cur, *processedPrev]

def testGetAddendsR():
    print('getAddends 2', getAddendsR(2))
    print('getAddends 3', getAddendsR(3))
    for i in range(4, 6):
        print('getAddends i', i, getAddendsR(i))

@track_performance
def euler76():
    print('project euler problem 76')
    print(len(getAddendsR(100)))

euler76()
# testGetAddendsR()
