print('project euler problem 31')

import copy

target = 200
coinsMatrix = [1, 2, 5, 10, 20, 50, 100]
maxMatrix = [200, 100, 40, 20, 10, 4, 2]

# iterate all permutations of the coins from 0 coins to max coins

def sumCoins(coins):
    sum = 0
    for i in range(len(coins)-1, -1, -1):
        if (sum > 200): 
          return 201
        sum += coinsMatrix[i] * coins[i]
    return sum


def getNextState(coins, skip = False): 
  for i in range(0, len(coins)):
    cur = coins[i]
    if cur < (maxMatrix[i]):
      for j in range(0, i):
        coins[j] = 0
      coins[i] += 1
      if skip:
        coins[i] = maxMatrix[i]
        return getNextState(coins, False)
      return coins
  return None


perms = [0, 0, 0, 0, 0, 0, 0]
res = 0
shouldSkip = False
while (True): 
  perms = getNextState(perms, shouldSkip)
  shouldSkip = False
  if (perms == None):
    break
  else:
    summed = sumCoins(perms)
    if summed == 200:
      res += 1
    if (summed > 200):
      shouldSkip = True

print('len is ', res)

