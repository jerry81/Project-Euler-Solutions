print('project euler problem 29')

def getPowerSequence(base, maxPower):
  res = set()
  for i in range(2, maxPower+1):
    exp = base**i
    res.add(exp)
  return res

finalSet = set()
for j in range(2, 101): 
  res = getPowerSequence(j, 100)
  finalSet = finalSet.union(res)
print('finalSet is {}'.format(len(finalSet)))