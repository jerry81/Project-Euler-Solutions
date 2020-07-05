print('project euler problem 28')

curDirection = 'E'

def getNextDirection():
  if (curDirection == 'E'):
    return 'S'
  if (curDirection == 'S'):
    return 'W'
  if (curDirection == 'W'):
    return 'N'
  else:
    return 'E'

def createSpiral(dim):
  spiralMap = {}
  x = 0
  y = 0
  cur = 1
  curDirection = 'E'
  if (dim == 1):
    spiralMap[x] = {}
    spiralMap[x][y] = cur
    cur += 1
  else: 
    if (curDirection == 'E'):
      x += 1
      try: spiralMap[x]
      except (NameError, KeyError) as e: spiralMap[x] = {}
      spiralMap[x][y] = cur
    elif (curDirection == 'S'):
      y -= 1
      spiralMap[x][y] = cur 
    elif (curDirection == 'W'): 
      x -= 1
      try: spiralMap[x]
      except (NameError, KeyError) as e: spiralMap[x] = {}
      spiralMap[x][y] = cur
    else: 
      y += 1
      spiralMap[x][y] = cur
    cur += 1
    for i in range(0, (dim - 1)): # repeat dim times
      print('working on i {}'.format(i))
    # go in curDirection cur times
  return spiralMap

res = createSpiral(2)
print('createSpiral result {}'.format(res))
print('curDir is', curDirection)
print ('nextDirecton is ', getNextDirection())