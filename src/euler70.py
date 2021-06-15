from utils.annotations import track_performance
from utils.myitertools import getFingerprint
from utils.toitientHelpers import getNonPrimeOddsToN, totient, getCandidates

def arePerms(a,b):
    return getFingerprint(int(a)) == getFingerprint(int(b))

# do primes' toitient values have any chance of being perm of the prime?

@track_performance
def euler70():
    print('project euler problem 70')
    ''' oddPrimes = getNonPrimeOddsToN(10000000, 9500000)
    permCandidates = []
    for pr in oddPrimes:
        toi = totient(pr)
        if arePerms(toi, pr):
            permCandidates.append((pr, toi, pr/toi))
    print('permCandidates are ', permCandidates)
    ''' 
    minimum = (1956103, 1953160.0, 1.0015067889983411)
    permCandidates = getCandidates()
    for item in permCandidates:
        toi = totient(item)
        _,_,curmin = minimum
        x,y,z = (item, toi, item/toi)
        if z < curmin:
            minimum = x,y,z
    print('min is ', minimum)
        

def testArePerms():
    print('arePerms 6, 60', arePerms(6,60))
    print('arePerms 6, 60', arePerms(71,22))
    print('arePerms 6, 60', arePerms(555,55))
    print('arePerms 6, 60', arePerms(112345,523141))

euler70()
# testArePerms()