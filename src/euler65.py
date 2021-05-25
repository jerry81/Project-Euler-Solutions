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
        
def testSeries():
    print('100 series is ', makeFractionSeriesForE(100))

@track_performance
def euler65():
    print('project euler problem 65')
    
euler65()
testSeries()
