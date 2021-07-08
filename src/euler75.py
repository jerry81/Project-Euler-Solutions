from utils.annotations import track_performance
from math import sqrt
from utils.fileUtils import writeMapToFile, openMap
from utils.toitientHelpers import getGCD

def getBGivenAAndT(a, t):
    d = t - a
    return (a**2 - d**2) / (-2 * d)

def isWhole(n):
    return int(n) == n

def getMaxA(t):
    return int((4*t - sqrt(8*t**2)) / 4)

def getSetOfIntegerSides(t):
    returned = []
    limA = int(getMaxA(t))
    count = 0
    for i in range(limA, 0, -1):
        b = getBGivenAAndT(i, t)
        if isWhole(b):
            returned.append({ i,b,sqrt(i**2+b**2) })
            count += 1
            """             if count > 1:
              return [] """
    return returned

def isOdd(n):
    return n%2 == 1 

def areCoprime(n,m):
    return getGCD(n,m) == 1

@track_performance
def euler75_2():
    print('project euler problem 75')
    LIM = 1500001
    UPPER_LIM_OUTER_LOOP = 2000
    countMap = {}
    for i in range(2, UPPER_LIM_OUTER_LOOP):
        for j in range(1, i):
            if isOdd(i) and isOdd(j):
                continue
            if not areCoprime(i, j):
                continue
            a,b,c = generateTriple(i,j)
            p = a+b+c
            if p < LIM:
              try:
                  t = countMap[p]
                  countMap[p] += 1
              except:
                  countMap[p] = 1
            # tally multiples
            multiple=2
            while True:
                a2,b2,c2 = a*multiple, b*multiple, c*multiple
                p2 = a2+b2+c2
                if p2<LIM:
                  try:
                    t = countMap[p2]
                    countMap[p2] += 1
                  except:
                    countMap[p2] = 1
                else:
                    break
                multiple += 1
    sliced = list(countMap.values())[:200]
    print('countMap is ', list(countMap.items())[:200])
    print('len of sliced is ', len(sliced))
    print('len of filtered slice is ', len(list(filter(lambda x: x==1, sliced))))
    print('count is ', len(list(filter(lambda x: x == 1, list(countMap.values())))))

@track_performance
def euler75():
    print('project euler problem 75')
    count = 0
    st = 1
    en = 1500000 // 2 + 1
    for i in range(st, en):
        x = i * 2
        if x % 10000 == 0:
            print('currently processing ', x)
        if x > 1500000:
            print('broke out. count is ', count)
        res = getSetOfIntegerSides(x)
        if len(res) == 1:
          count += 1
    print('count is ', count)
    # brute force chunking

def testIsWhole():
    print('isWhole 7.0', isWhole(7.0))
    print('isWhole 5/2', isWhole(5/2))
    print('isWhole 6/2', isWhole(6/2))

def testGetB():
    print('getB 3 12', getBGivenAAndT(3, 12))
    print('getB 2 12', getBGivenAAndT(2, 12))
    print('getB 6, 24', getBGivenAAndT(6,24))
    print('getB 20, 120', getBGivenAAndT(20, 120))
    print('getB 35, 120', getBGivenAAndT(35, 120))
    for i in range(1, 35):
      print('getB i, 120', i, getBGivenAAndT(i, 120))

def testGetSet():
    print('getSet 12', getSetOfIntegerSides(12))
    print('getSet 24', getSetOfIntegerSides(24))
    print('getSet 30', getSetOfIntegerSides(30))
    print('getSet 36', getSetOfIntegerSides(36))
    print('getSet 40', getSetOfIntegerSides(40))
    print('getSet 48', getSetOfIntegerSides(48))
    print('getSet 60', getSetOfIntegerSides(48))
    print('getSet 72', getSetOfIntegerSides(48))
    print('getSet 120', getSetOfIntegerSides(120))
    print('getSet 1200', getSetOfIntegerSides(1200))
    print('getSet 240', getSetOfIntegerSides(240))
    print('getSet 300', getSetOfIntegerSides(300))
    print('getSet 360', getSetOfIntegerSides(360))
    print('getSet 400', getSetOfIntegerSides(400))
    print('getSet 80', getSetOfIntegerSides(80))
    print('getSet 800', getSetOfIntegerSides(800))
    print('getSet 8000', getSetOfIntegerSides(8000))
    print('getSet 480', getSetOfIntegerSides(480))
    print('getSet 2400', getSetOfIntegerSides(2400))
    print('getSet 3000', getSetOfIntegerSides(3000))
    print('getSet 3600', getSetOfIntegerSides(3600))
    print('getSet 4000', getSetOfIntegerSides(4000))
    print('getSet 4800', getSetOfIntegerSides(4800))
    print('getSet 12000', getSetOfIntegerSides(12000))
    print('getSet 40000', getSetOfIntegerSides(40000))
    print('getSet 400000', getSetOfIntegerSides(400000))
    print('getSet 1500000', getSetOfIntegerSides(1500000))

@track_performance
def getFilteredList():
    # read from file
    seive = {}
    print('seive initialized')
    for j in range(0,10000):
        if (j%1000 == 0):
            print('currently processing ', j)
        k = j*2
        if seive[str(k)] != None:
            continue
        curSet = getSetOfIntegerSides(k)
        if len(curSet) == 1:
            seive[str(k)] = True 
            markMultiples(seive, k, 1500000)
        else:
            seive[str(k)] = False
    # filter out False 
    remainingItems = list(filter(lambda x: x[1] != False, list(seive.items())))
    # write to file
    # writeMapToFile('0to10000Processed.txt', seive)
    remainingNones = len(list(filter(lambda x: x[1] == None, remainingItems)))
    trues = len(list(filter(lambda x: x[1] == True, remainingItems)))
    print('remainingItems', remainingNones)

def markMultiples(sv, seed, lim):
    multiplier = 2
    bust = False
    while True:
        cur = multiplier * seed
        if cur > lim:
            return
        if sv[str(cur)] != None:
            multiplier += 1
            continue
        if bust == True:
            sv[str(cur)] = False
        else:
            setOne = getSetOfIntegerSides(cur)
            if len(setOne) == 1:
                sv[str(cur)] = True
            else:
                sv[str(cur)] = False
                bust = True
        multiplier += 1
        

def testAllSets():
        allSets = []
        nonZero = []
        for t in range(1, 5000):
          curSet = getSetOfIntegerSides(t)
          if len(curSet) == 1:
              allSets.append(t)
          elif len(curSet) != 0:
            nonZero.append(t)
        print('allSets is ', allSets)
        print('nonZero are ', nonZero)

def testGetMax():
    print('getMax 12', getMaxA(12))
    print('getMax 24', getMaxA(24))
    print('getMax 30', getMaxA(30))
    print('getMax 36', getMaxA(36))
    print('getMax 40', getMaxA(40))
    print('getMax 48', getMaxA(48))
    print('getMax 120', getMaxA(120))
    print('getmax 1500000', getMaxA(1500000))

def generateTriple(m,n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a,b,c

def getPerimiter(m,n):
    a,b,c = generateTriple(m,n)
    return a+b+c

def testGenerateTriples():
    for i in range(2, 10):
        for j in range(1, i):
            a,b,c = generateTriple(i, j)
            print('given i, j, triple is, sum is  ', i, j, (a,b,c), sum([a,b,c]))

def testLimitsAndPerf():
    print('getPerimiter 7500, 7499', getPerimiter(7500, 7499))
    print('getPerimiter 866 is ', getPerimiter(866, 1))
    

@track_performance
def stress():
    for i in range(1499950, 1500001):
        res = getSetOfIntegerSides(i)
        if len(res) == 1:
          print('getSet i is ', i, getSetOfIntegerSides(i))

# euler75()
# testIsWhole()
# testGetB()
# testGetSet()
# testGetMax()
# stress()
# testAllSets()
# getFilteredList()
# testGenerateTriples()
# testLimitsAndPerf()
euler75_2()

def testIsOdd():
    print('isOdd 3', isOdd(3))
    print('isOdd 19999', isOdd(19999))
    print('isOdd 1000', isOdd(1000))

# testIsOdd()

def testAreCoprime():
    print('coprime 3,5', areCoprime(3,5))
    print('coprime 11,40', areCoprime(11,40))
    print('coprime 8,20', areCoprime(8,20))
    print('coprime 12,15', areCoprime(12,15))
    print('coprime 88, 87', areCoprime(88,87))
    print('coprime 121 22', areCoprime(121, 44))

# testAreCoprime()