from utils.annotations import track_performance

def getNForDCloseTo3over7(d):
    return (3 * d) // 7

@track_performance
def euler71():
    minDiff = 1000000
    candidate = 0
    candidated = 0
    print('project euler problem 71')
    for d in range(1, 1000001):
        n = getNForDCloseTo3over7(d)
        if (n == 3 and d == 7):
            continue
        dec = n / d
        diff = (3/7) - dec
        if diff == 0:
            continue 
        if diff < minDiff:
            minDiff = diff 
            candidate = n
            candidated = d
    print('n is ', candidate, candidated)

euler71()