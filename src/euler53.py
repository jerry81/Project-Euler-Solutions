from utils.annotations import track_performance
import math

print('project euler problem 53')

def rFromN(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial((n-r)))

@track_performance
def euler53():
    count = 0
    for i in range (1, 101):
        for j in range (1, i):
          if (rFromN(i, j) > 1000000):
              count += 1
    print('count is ', count)
euler53()
