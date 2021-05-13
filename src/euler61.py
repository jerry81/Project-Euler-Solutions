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
  sub = allTests[:3]
  for a in range(10,100):
    for b in range(10,100):
      num1 = str(a) + str(b)
      result = allInSet(sub, [num1])
      if len(list(result.keys())) != 1:
        continue
      for c in range(10,100):
          num2 = str(b) + str(c)
          num3 = str(c) + str(a)
          result = allInSet(sub, [num1, num2, num3])
          if len(set(flattenLists(result.values()))) == 3:
            print('result is ', result)

def flattenLists(lists):
  return [j for i in lists for j in i]

def pick6Of89():
  sub = allTests
  for a in range(10,100):
    for b in range(10,100):
      num1 = str(a) + str(b)
      result = allInSet(sub, [num1])
      if (len(list(result.keys()))) != 1:
        continue
      for c in range(10,100):
        num2 = str(b) + str(c)
        result = allInSet(sub, [num2])
        if len(list(result.keys())) !=1:
          continue
        for d in range(10,100):
          num3 = str(c) + str(d)
          result = allInSet(sub, [num3])
          if len(list(result.keys())) !=1:
            continue
          for e in range(10,100):
            num4 = str(d) + str(e)
            result = allInSet(sub, [num4])
            if len(list(result.keys())) !=1:
              continue
            for f in range(10,100):
              num5 = str(e) + str(f)
              num6 = str(f) + str(a)
              result = allInSet(sub, [num1, num2, num3, num4, num5, num6])
              #if len(list(result.keys())) == 6 and len(set(flattenLists(result.values()))) == 6:
              if len(list(result.keys())) == 6:
                print('result is ', result)

def allInSet(setC, inputs):
  resultMap = {}
  for num in inputs:
    for idx, s in enumerate(setC):
      if checkMap(num, s):
        if checkMap(num, resultMap):
          resultMap[num].append(idx)
          resultMap[num] = list(set(resultMap[num]))
        else: 
          resultMap[num] = [idx]
  return resultMap

def testAllInSet():
  set1 = ['8128', '2882', '8281']
  print('result test is: ', allInSet(allTests, set1))


@track_performance
def euler61():
  print('project euler problem 61')
  # pick3Of89()
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
