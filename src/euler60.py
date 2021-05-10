from utils.annotations import track_performance
from filterArrayAndOutput import primeMap
import binascii

def checkPrime(num):
  return str(num) in primeMap.keys()

def pick4ofX(limSet):
  # perms
  for a in range(limSet - 3):
    for b in range(a + 1, limSet - 2):
      for c in range(b + 1, limSet - 1):
        for d in range(c + 1, limSet):
          print('abcd',a,b,c,d)
          # checkConcatenations4(a,b,c,d)
          
def checkConcatenations4(a,b,c,d):
  pass

def testPick4():
  pick4ofX(10)

def testCheckPrime():
  print('check prime Prime', checkPrime(15092801))
  print('check prime not Prime', checkPrime(2222))

@track_performance
def euler60():
  print('project euler problem 60')

euler60()
testCheckPrime()
testPick4()