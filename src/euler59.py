from utils.annotations import track_performance
from utils.fileUtils import openAndSplit
import binascii

asArr = openAndSplit('./resources/p059_cipher.txt')
print('asArr', asArr)
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

@track_performance
def euler59():
  print('project euler problem 59')

euler59()
testStoA()
testAtoS()