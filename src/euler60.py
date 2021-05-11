from utils.annotations import track_performance
from filterArrayAndOutput import primeMap
import binascii

keys = list(map(lambda x: int(x), primeMap.keys()))

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
    if not checkPrime(c):
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
      for c in range(b + 1, limSet - 1):
        for d in range(c + 1, limSet):
          toCheck = list(map(lambda x: keys[x],[a,b,c,d]))
          if not checkConcatenations(toCheck):
            continue
          print('candidates found', toCheck)

def testPick4():
  pick4ofX(10)

def testCheckPrime():
  print('check prime Prime', checkPrime(15092801))
  print('check prime not Prime', checkPrime(2222))

@track_performance
def euler60():
  print('project euler problem 60')
  pick4ofX(10)

euler60()
# testCheckPrime()
# testPick4()
# testConcatenations()
# testAssemble()