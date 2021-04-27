from utils.annotations import track_performance
from utils.stringHelpers import isPalindrome

def reverseAndAdd(number):
  s = str(number)
  r = list(s)
  r.reverse()
  r = ''.join(r)
  return int(s) + int(r)

def isLychrel(number, limit = 50):
  for i in range(limit):
    s = reverseAndAdd(number)
    if isPalindrome(str(s)):
      return False
    number = s
  return True

def testReverseAndAdd():
  n1 = 47
  print('121 is ', reverseAndAdd(n1))
  n2 = 349
  print('1292 is ', reverseAndAdd(n2))
  n3 = 1292
  print('4213 is ', reverseAndAdd(n3))

def testIsLychrel():
  n1 = 47
  n2 = 349
  n3 = 196
  print('False is ', isLychrel(n1))
  print('False is ', isLychrel(n2))
  print('True is ', isLychrel(n3))

print('project euler problem 55')

@track_performance
def euler55():
  print('starting 55')
  LIMIT = 10000
  cnt = 0
  for i in range(LIMIT):
    if isLychrel(i):
      cnt+=1
  print('count is ', cnt)

testReverseAndAdd()
testIsLychrel()
euler55()