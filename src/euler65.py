from utils.annotations import track_performance

def makeFractionSeriesForE(lim):
    res = [1]
    for i in range(lim-1):
        dividend = int(i / 3)
        rem = i % 3
        ev = 2 * (dividend + 1)
        if rem == 0:
            res.append(ev)
        else:
            res.append(1)
    return res

def getRecurrentFractionForE(atIdx):
    if atIdx == 0:
        return 2, 1
    seriesLim = atIdx - 1
    series = makeFractionSeriesForE(seriesLim)
    while series:
        item = series.pop()
        print('item is ', item)
    print('series is ', series)
            
def testSeries():
    print('10 series is ', makeFractionSeriesForE(10))
    print('100 series is ', makeFractionSeriesForE(100))

def testRecurrentFractionForE():
    print('recurrent 1 is ', getRecurrentFractionForE(1))

@track_performance
def euler65():
    print('project euler problem 65')
    
euler65()
testSeries()
testRecurrentFractionForE()