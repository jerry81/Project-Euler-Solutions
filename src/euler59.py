from utils.annotations import track_performance
from utils.fileUtils import openAndSplit
import binascii

asArr = openAndSplit('./resources/p059_cipher.txt')
asIntArr = list(map(lambda x: int(x), asArr))
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
  a = 65
  b = 42
  c = 107
  print('a ^ b = c', a ^ b)
  print('c ^ b = a', c ^ b)
  # print('xor should be {} - {}'.format(expected, bin(ord(s1)) ^ bin(ord(key1))))

# key is array of ascii codes between a-z 97 to 123
def decypher(key):
  output = []
  for i in range(len(asIntArr)):
    toDecode = asIntArr[i]
    decoded = toDecode ^ key[i % 3]
    output.append(chr(decoded))
  return output

def checkFirstWord(charArr):
  for i in range(len(charArr)):
    if not charArr[i].isalpha():
      return charArr[0:i]

def checkFirstNWords(charArr, n):
  count = 0
  for i in range(len(charArr)):
    if not charArr[i].isalpha():
      count += 1
      if count >= n:
        return charArr[0:i]

def testDecypher():
  arr = decypher([ord('e'), ord('x'), ord('p')])
  asciArr = list(map(lambda x: ord(x), arr))
  print('arr is ', asciArr)
  print('sum is ', sum(asciArr))

@track_performance
def euler59():
  print('project euler problem 59')
  f2 = open("./resources/59_outputs.txt", "x+")
  for i in range(97, 123):
    for j in range(97, 123):
      for k in range(97, 123):
        ch = decypher([i,j,k])
        firstWord = checkFirstWord(ch)
        # if len(firstWord) == 1 and firstWord[0] != 'I' and firstWord[0] != 'A':
        #  continue
        if len(firstWord) == 0:
          continue
        threeWords = checkFirstNWords(ch, 20)
        f2.write(''.join([str(chr(i)),str(chr(j)),str(chr(k))]))
        f2.write('   ')
        f2.write("".join(threeWords))
        f2.write('\n')
  f2.close()

print('xor test 0bx0 is', bin(97 ^ 97))
print('xor test 0bx11 is ', bin(97 ^ 98))



# euler59()
testStoA()
testAtoS()
testAtoB()
testBtoA()
testXOR()
testDecypher()