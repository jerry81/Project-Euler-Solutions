from math import sqrt
from utils.mathHelpers import isPrime
print('project euler problem 48')

oneThruTen = 10405071317
tenThruTwenty = 106876212200059553898143707

def powerSeries(fr, to):
  res = 0
  for i in range(fr, to+1):
    res+= i**i
  return res

print(powerSeries(1, 1000))

