from utils.annotations import track_performance
from utils.toitientHelpers import totient, o1isPrime

@track_performance
def euler72():
    print('project euler problem 72')
    tot = 300923901638.0
    for d in range(2, 100001):
      if o1isPrime(d):
          tot += d - 1
          continue
      tot += totient(d)
    print('tot is ', tot)      

# euler72()

@track_performance
def perfTest():
    result = 0
    seive = list(range(9))
    for i in range(2,9):
        if seive[i] == i:
          for j in range(i, 9, i):
              seive[j] = seive[j] / i * (i-1)
        result += seive[i]
    print('result is ', result)
    print('seive is now ', seive)
perfTest()