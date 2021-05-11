from utils.annotations import track_performance
from filterArrayAndOutput import primeMap
import binascii

keys = list(map(lambda x: int(x), primeMap.keys()))
memo = {} # { 122: False }

def checkMemo(num):
  value = memo.get(num, None)
  if value is not None:
    return value
  memo[num] = checkPrime(num)
  return memo[num]

def checkPrime(num):   
  value = primeMap.get(num, None)
  if value is not None: 
    return True
  return False
  # return num in keys # is this O(1)? - no - keys is an array

def checkConcatenations(inputs):
  candidates = []
  for a in range(len(inputs) - 1):
    for b in range(a + 1, len(inputs)):
      cands = assembleCandidate(inputs[a],inputs[b])
      for cd in cands:
        candidates.append(cd)
  for c in candidates:
    if not checkMemo(c):
      return False
  return True

def assembleCandidate(a,b):
  f = int(str(a) + str(b))
  r = int(str(b) + str(a))
  return [f,r]

def testAssemble():
  assembleCandidate(7, 109)

def testConcatenations():
  print('1,2,3,4 is ', checkConcatenations([1,2,3,4]))
  print('10,11,12,13,14 is ', checkConcatenations([10,11,12,13,14]))

def pick4ofX(limSet):
  # perms
  for a in range(limSet - 3):
    for b in range(a + 1, limSet - 2):
      if not checkConcatenations([keys[a],keys[b]]):
        continue
      for c in range(b + 1, limSet - 1):
        if not checkConcatenations([keys[a],keys[b],keys[c]]):
          continue
        for d in range(c + 1, limSet):
          toCheck = list(map(lambda x: keys[x],[a,b,c,d]))
          if not checkConcatenations(toCheck):
            continue
          print('candidates found', toCheck)

def pick5ofX(limSet):
  # perms
  for a in range(limSet - 4):
    for b in range(a + 1, limSet - 3):
      toCheck = list(map(lambda x: keys[x],[a,b]))
      if not checkConcatenations(toCheck):
        continue
      for c in range(b + 1, limSet - 2):
        toCheck = list(map(lambda x: keys[x],[a,b,c]))
        if not checkConcatenations(toCheck):
          continue
        for d in range(c + 1, limSet -1):
          toCheck = list(map(lambda x: keys[x],[a,b,c,d]))
          if not checkConcatenations(toCheck):
            continue
          for e in range(d + 1, limSet):
            toCheck = list(map(lambda x: keys[x],[a,b,c,d,e]))
            if not checkConcatenations(toCheck):
              continue
            print('candidates found', toCheck)

def pick1(limSet):
  for a in range(limSet):
    toCheck=[3,7,109,673,keys[a]]
    if not checkConcatenations(toCheck):
      continue
    print('candidates found', keys[a])

def testPick4():
  pick4ofX(10)

def testCheckPrime():
  print('check prime Prime', checkPrime(15092801))
  print('check prime not Prime', checkPrime(2222))

def testCheckMemo():
  print('check prime Prime', checkMemo(15092801))
  print('check prime not Prime', checkMemo(2222))
  print('not prime', checkMemo(124))
  print('memo is now ', memo)
  print('check prime Prime', checkMemo(15092801))
  print('check prime not Prime', checkMemo(2222))
  print('not prime', checkMemo(124))

@track_performance
def euler60():
  print('project euler problem 60')
  # print('check', checkConcatenations([3,7,109,673]))
  # pick1(9000000)
  pick5ofX(1000)

euler60()
# testCheckPrime()
# testPick4()
# testConcatenations()
# testAssemble()
# testCheckMemo()