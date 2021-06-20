from utils.annotations import track_performance
from math import factorial

def getNextIter(num):
    asList = list(str(num))
    s = 0
    for ch in asList:
        asInt = int(ch)
        s += factorial(asInt)
    return s


@track_performance
def euler74():
    print('project euler problem 74')
   
def testGetNextIter():
    print('nextIter 145', getNextIter(145))

euler74()
testGetNextIter()