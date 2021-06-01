from utils.annotations import track_performance
from utils.fileUtils import openAndSplitPlus

def condenseTriangle(triangle):
    lastRow = len(triangle) - 1
    secondToLastRow = len(triangle) - 2
    if secondToLastRow < 0:
        return
    copied = triangle.copy()
    copied.pop()
    second = triangle[secondToLastRow]
    last = triangle[lastRow]
    for i in range(0, len(second)):
        cur = int(second[i])
        maxChild = max([int(last[i]), int(last[i+1])])
        copied[secondToLastRow][i] = cur + maxChild
    return copied

def fullyCondenseTriangle():
    triangleLines = openAndSplitPlus('./resources/p067_triangle.txt', '\n')
    noEmpty = list(filter(lambda x: len(x) > 0, triangleLines))
    asArr = list(map(lambda x: x.split(' '), noEmpty))
    condensed = condenseTriangle(asArr)
    copied = condensed.copy()
    while True:
        nextCondensed = condenseTriangle(copied)
        if (not nextCondensed):
            return copied
        copied = nextCondensed


def testCondense():
    triangleLines = openAndSplitPlus('./resources/p067_triangle.txt', '\n')
    noEmpty = list(filter(lambda x: len(x) > 0, triangleLines))
    asArr = list(map(lambda x: x.split(' '), noEmpty))
    print('asArr is ', asArr, len(asArr))
    condensed = condenseTriangle(asArr)
    print('condensed is ', condensed, len(condensed))

@track_performance
def euler67():
    triangleLines = openAndSplitPlus('./resources/p067_triangle.txt', '\n')
    noEmpty = list(filter(lambda x: len(x) > 0, triangleLines))
    asArr = list(map(lambda x: x.split(' '), noEmpty))
    print('project euler problem 67')
    fullyCondensedTriangle = fullyCondenseTriangle()
    print('fullyCondensedTriangle', fullyCondensedTriangle)


euler67()
# testCondense()