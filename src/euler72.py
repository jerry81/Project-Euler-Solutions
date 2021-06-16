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

euler72()