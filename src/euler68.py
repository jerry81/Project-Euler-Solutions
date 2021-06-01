from utils.annotations import track_performance
from itertools import permutations

threeGon = [
    [0,1,2],
    [3,2,4],
    [5,4,1]
]

oneToSix = list(range(1,7))
print('oneToSix ', oneToSix)

perms = list(map(lambda x: list(x), list(permutations(oneToSix))))


print('perms are ', perms)

@track_performance
def euler68():
    print('project euler problem 68')


euler68()