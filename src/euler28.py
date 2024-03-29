print('project euler problem 28')

def getNextDirection(curDirection):
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
  for i in range(0, dim): # repeat dim times
    if (i == 0):
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
      curDirection = getNextDirection(curDirection)
      for a in range(0, 2):
        for j in range(0, i):
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
        if a == 0:
          curDirection = getNextDirection(curDirection)
    # go in curDirection cur times
  return spiralMap

def sumDiagonals(map, dim):
  min = (dim // 2) * -1
  max = (dim // 2)
  sum = 0
  for i in range(min, max + 1):
    sum += map[i][i]
    sum += map[i][-i]
  return sum - 1
  
res = createSpiral(1001)
sum = sumDiagonals(res, 1001)
print('sum is {}'.format(sum))