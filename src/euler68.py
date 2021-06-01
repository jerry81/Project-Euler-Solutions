from utils.annotations import track_performance
from itertools import permutations

threeGon = [
    [0,1,2],
    [3,2,4],
    [5,4,1]
]

fiveGon = [
    [0,1,2],
    [3,2,4],
    [5,4,6],
    [7,6,8],
    [9,8,1]
]

oneToSix = list(range(1,7))

oneToTen = list(range(1, 11))

perms = list(map(lambda x: list(x), list(permutations(oneToSix))))

perms10 = list(map(lambda x: list(x), list(permutations(oneToTen))))

print('perms10 len is ', len(perms10))

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

solutions = [197438, 277699, 347135, 355389, 480326, 515672, 592124, 600303, 633690, 664678, 700024, 711999, 842019, 843949, 959461, 1034541, 1060360, 1060403, 1200461, 1282003, 1383557, 1393699, 1487016, 1598835, 1600765, 1638613, 1710610, 1710653, 1716303, 1778243, 1850556, 1912496, 1918146, 1918189, 1990186, 2028034, 2029964, 2141783, 2235100, 2245242, 2346796, 2428338, 2568396, 2568439, 2594258, 2669338, 2784850, 2786780, 2916800, 2928775, 2964121, 2995109, 3028496, 3036675, 3113127, 3148473, 3273410, 3281664, 3351100, 3431361]

def testAddUpLines():
    print('addupLines is, threeGon, 123456', addUpLines(threeGon, perms[0]))
    print('addUpLines is, threeGon, 432615', addUpLines(threeGon, [4,3,2,6,1,5]))
    print('addUpLines is, threeGon, 235416', addUpLines(threeGon, [2,3,5,4,1,6]))
    print('addupLines, 5gon, index 197438 is ', perms10[197438], addUpLines(fiveGon, perms10[197438]))

def get5GonSolutions():
    results = []
    idx = 0
    for p in perms10:
        res = addUpLines(fiveGon, p)
        if res:
          results.append(idx)
        idx+=1
    return results 

@track_performance
def euler68():
    print('project euler problem 68')
    maxT = 0
    perms = list(map(lambda x: perms10[x],solutions))
    fiveGons = []
    for i in perms:
      cur = []
      for j in fiveGon:
          for k in j:
              cur.append(i[k])
      fiveGons.append(cur)
    for i in fiveGons:
        asStr = list(map(lambda x: str(x), i))
        joined = ''.join(asStr)
        print('asStr is ', joined)
        if len(joined) == 16 and int(joined) > maxT:
            maxT = int(joined)
    print('maxT', maxT)

euler68()
# testAddUpLines()