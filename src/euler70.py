from utils.annotations import track_performance
from utils.myitertools import getFingerprint

def arePerms(a,b):
    return getFingerprint(a) == getFingerprint(b)

# do primes' toitient values have any chance of being perm of the prime?

@track_performance
def euler70():
    print('project euler problem 70')

def testArePerms():
    print('arePerms 6, 60', arePerms(6,60))
    print('arePerms 6, 60', arePerms(71,22))
    print('arePerms 6, 60', arePerms(555,55))
    print('arePerms 6, 60', arePerms(112345,523141))

euler70()
testArePerms()