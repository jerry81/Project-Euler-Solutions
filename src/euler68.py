from utils.annotations import track_performance
from itertools import permutations

threeGon = [
    [0,1,2],
    [3,2,4],
    [5,4,1]
]

oneToSix = list(range(1,7))
print('oneToSix ', oneToSix)

perms = list(map(lambda x: list(x), list(permutations(oneToSix))))


print('perms are ', perms)

def addUpLines(xGon, cur):
    tSum = 0
    mSum = 0
    for i in xGon:
        line = list(map(lambda x: cur[x], i))
        cSum = sum(line)
        if mSum != 0 and cSum != mSum:
            return
        mSum = cSum
        tSum += cSum
    return mSum

def testAddUpLines():
    print('addupLines is, threeGon, 123456', addUpLines(threeGon, perms[0]))
    print('addUpLines is, threeGon, 432615', addUpLines(threeGon, [4,3,2,6,1,5]))
    print('addUpLines is, threeGon, 235416', addUpLines(threeGon, [2,3,5,4,1,6]))

@track_performance
def euler68():
    print('project euler problem 68')


euler68()
testAddUpLines()