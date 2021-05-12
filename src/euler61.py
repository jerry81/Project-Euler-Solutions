from utils.annotations import track_performance
from utils.fileUtils import openMap

triangles = openMap('./resources/triangleMap.txt')

squares = openMap('./resources/squares.txt')

pent = openMap('./resources/pentagonal.txt')

hexa = openMap('./resources/hexa.txt')

hep = openMap('./resources/hep.txt')

octa = openMap('./resources/octa.txt')

allTests = [triangles, squares, pent, hexa, hep, octa]

def pick4Of89():
  for a in range(10,99):
    for b in range(10,99):
      for c in range(10,99):
        for d in range(10,99):
          num1 = str(a) + str(b)
          num2 = str(b) + str(c)
          num3 = str(c) + str(d)
          num4 = str(d) + str(a)
          print('numbers are ', num1,num2,num3,num4)

@track_performance
def euler61():
  print('project euler problem 61')
  pick4Of89()

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
# testCheckmap()
