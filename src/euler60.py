from utils.annotations import track_performance
from filterArrayAndOutput import primeMap
import binascii

def checkPrime(num):
  return str(num) in primeMap.keys()

def checkConcatenations(inputs):
  for a in range(len(inputs) - 1):
    for b in range(a + 1, len(inputs)):
      print('ab are ', a,b)

def testConcatenations():
  checkConcatenations([1,2,3,4])
  checkConcatenations([10,11,12,13,14])

def pick4ofX(limSet):
  # perms
  for a in range(limSet - 3):
    for b in range(a + 1, limSet - 2):
      for c in range(b + 1, limSet - 1):
        for d in range(c + 1, limSet):
          print('abcd',a,b,c,d)
          # checkConcatenations([a,b,c,d])
          

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
testConcatenations()