from utils.annotations import track_performance

print('project euler problem 56')

def longMultiplication(a,b):
  arrA = map(lambda x: int(x), list(a))
  arrB = map(lambda x: int(x), list(b))
  revA = arrA
  revB = arrB
  revA.reverse()
  revB.reverse()


def sumDigits(input):
  asArr = map(lambda x: int(x), list(input))
  return sum(asArr)

def testSumDigits():
  input1 = '12345'
  print('15 is ', sumDigits(input1))
  input2 = '100000'
  print('1 is ', sumDigits(input2))

@track_performance
def euler56():
  LIMIT = 100
  maximum = 0
  for i in range(LIMIT):
    for j in range(LIMIT):
      prod = i ** j
      digitalSum = sumDigits(str(prod))
      print('digitalSum is ', digitalSum)
      if int(digitalSum) > maximum:
        print('resetting')
        maximum = int(digitalSum)
  print('max is ', maximum)

euler56()
testSumDigits()