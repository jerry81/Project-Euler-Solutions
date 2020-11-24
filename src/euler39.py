print('project euler problem 39')

# right angle triangle - a**2 + b**2 = c**2

def isRightTriangle(a, b, c):
  return a**2 + b**2 == c**2

print("is right", isRightTriangle(3,4,5))
print("is right", isRightTriangle(20,48,52))
print("isn't right", isRightTriangle(1,5,9))

def isTupleRightTriangle(object): 
  res = isRightTriangle(object["a"], object["b"], object["c"])
  return res

# all combinations summing up to x
# 3 for loops 
# smallest perimeter 6 (1+2+3)
# first = 1 to x-4
# second = first+1 to x-3
# third = second+1 to x-2

def getAllCombinations(x): 
  combos = []
  for a in range(1, (x//3)+1):
    for b in range(a, (x//2)+1):
      c = x - (a+b)
      if (a <= b and b <= c):
        combos.append({"a": a,"b": b,"c": c})
  return combos

highest = { 'idx': 1, 'cnt': 0 }
for i in range(1, 1001):
  combos = getAllCombinations(i)
  filteredCombos = filter(isTupleRightTriangle, list(combos))
  comboCount = len(list(filteredCombos))
  if (comboCount > highest['cnt']):
    highest['idx'] = i
    highest["cnt"] = comboCount
    print('highest is ', highest)