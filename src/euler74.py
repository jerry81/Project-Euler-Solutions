from utils.annotations import track_performance
from math import factorial

def getNextIter(num):
    asList = list(str(num))
    s = 0
    for ch in asList:
        asInt = int(ch)
        s += factorial(asInt)
    return s

def inMap(x, m):
    try: 
        y = m[x]
        return True
    except:
        return False

def iterUntilRepeat(starting):
    repeats = {str(starting):True}
    nxt = starting
    while True:
        nxt = getNextIter(nxt)
        if inMap(nxt, repeats):
            return repeats, nxt
        repeats[nxt] = True

@track_performance
def euler74():
    print('project euler problem 74')
    hitcount = 0
    for i in range(1, 1000000):
        arr, last = iterUntilRepeat(i)
        if len(arr) == 60:
            hitcount += 1
    print('hitCount is ', hitcount)

def testGetNextIter():
    print('nextIter 145', getNextIter(145))

def testIterUntilRepeat():
    print('iur 69', iterUntilRepeat(69))

euler74()
# testGetNextIter()
# testIterUntilRepeat()