from utils.annotations import track_performance
from utils.stringHelpers import isPalindrome

def reverseAndAdd(number):
  s = str(number)
  r = list(s)
  print('r is ', r)
  r.reverse()
  r = ''.join(r)
  print('s is ', s)
  print('r is ', r)
  return int(s) + int(r)

def testReverseAndAdd():
  n1 = 47
  print('121 is ', reverseAndAdd(n1))
  n2 = 349
  print('1292 is ', reverseAndAdd(n2))
  n3 = 1292
  print('4213 is ', reverseAndAdd(n3))

print('project euler problem 55')

@track_performance
def euler55():
  print('starting 55')

testReverseAndAdd()
euler55()