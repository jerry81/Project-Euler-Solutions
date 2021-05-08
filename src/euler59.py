from utils.annotations import track_performance
from utils.fileUtils import openAndSplit
import binascii

asArr = openAndSplit('./resources/p059_cipher.txt')
asCharArr = list(map(lambda x: chr(int(x)), asArr))
print('asArr', asCharArr)
def stoa(s):
  charArr = list(s)
  return list(map(lambda x: ord(x),charArr))

def atos(a):
  return list(map(lambda x: chr(x), a))

# helper convert ascii to char

# string to binary 
# binascii.a2b_uu(string)

# binary to ascii
# binascii.b2a_uu(bytes)

# helper convert ascii to bits
# helper xor on bits 

# helper to decrypt with a 3 letter key
# loop through all 26 lowercase characters for strings of length 3 until a sensible message appears

def testAtoB():
  print('a to b a', "{0:b}".format((97)))
  print('a to b b', "{0:b}".format(ord('b')))

def testBtoA():
  print('b to a a', chr(int('1100001', 2)))

def testStoA():
  source = 'abc'
  print('to ascii is ', stoa(source))
  source2 = 'def'
  print('testAtoB is ', stoa(source2))

def testAtoS():
  source = [97, 98, 99]
  source2 = [100, 101, 102]
  print('to char arr abc is ', atos(source))
  print('def is ', atos(source2))

def testXOR():
  s1 = 'a'
  key1 = 'a'
  expected = '0000000'
  # print('xor should be {} - {}'.format(expected, bin(ord(s1)) ^ bin(ord(key1))))

@track_performance
def euler59():
  print('project euler problem 59')

print('xor test 0bx0 is', bin(97 ^ 97))
print('xor test 0bx11 is ', bin(97 ^ 98))

euler59()
testStoA()
testAtoS()
testAtoB()
testBtoA()
testXOR()