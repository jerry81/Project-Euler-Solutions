from utils.annotations import track_performance
from utils.toitientHelpers import totient

@track_performance
def euler72():
    print('project euler problem 72')
    tot = 3039650754
    for d in range(100001, 200001):
      tot += totient(d)
    print('tot is ', tot)      

euler72()