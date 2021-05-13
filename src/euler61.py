from utils.annotations import track_performance
from utils.fileUtils import openMap

triangles = openMap('./resources/triangleMap.txt')

squares = openMap('./resources/squares.txt')

pent = openMap('./resources/pentagonal.txt')

hexa = openMap('./resources/hexa.txt')

hep = openMap('./resources/hep.txt')

octa = openMap('./resources/octa.txt')

allTests = [triangles, squares, pent, hexa, hep, octa]

def pick3Of89():
  for a in range(10,99):
    for b in range(10,99):
      for c in range(10,99):
          num1 = str(a) + str(b)
          num2 = str(b) + str(c)
          num3 = str(c) + str(a)
          sub = allTests[:3]
          result = allInSet(sub, [num1, num2, num3])
          if len(set(result.values())) == 3:
            print('result is ', result)

def pick6Of89():
  sub = allTests
  for a in range(10,100):
    for b in range(10,100):
      num1 = str(a) + str(b)
      for c in range(10,100):
        num2 = str(b) + str(c)
        last = str(c) + str(a)
        for d in range(10,100):
          num3 = str(c) + str(d)
          last = str(d) + str(a)
          for e in range(10,100):
            num4 = str(d) + str(e)
            last = str(e) + str(a)
            for f in range(10,100):
              print('got to 5')
              num5 = str(e) + str(f)
              num6 = str(f) + str(a)
              result = allInSet(sub, [num1, num2, num3, num4, num5, num6])
              if len(set(result.values())) == 6:
                print('result is ', result)

def allInSet(setC, inputs):
  resultMap = {}
  for num in inputs:
    for idx, s in enumerate(setC):
      if checkMap(num, s):
        resultMap[num] = idx
  return resultMap

def testAllInSet():
  set1 = ['8128', '2882', '8281']
  print('result test is: ', allInSet(allTests, set1))


@track_performance
def euler61():
  print('project euler problem 61')
  pick6Of89()

def checkMap(num, _map):
  value = _map.get(num, None)
  if value is not None:
    return True
  return False

def testCheckmap():
  test1 = '8128'
  test2 = '2882'
  test3 = '8281'
  print('test1 is True', checkMap(test1, triangles))
  print('test2 is True', checkMap(test2, pent))
  print('test3 is True', checkMap(test3, squares))
  print('test4 is FAlse', checkMap('17', triangles))
  print('test5 is FAlse', checkMap('17', squares))
  print('test6 is FAlse', checkMap('17', pent))


euler61()
testAllInSet()
# testCheckmap()
