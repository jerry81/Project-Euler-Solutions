print('project euler problem 28')

def createSpiral(dim):
  spiralMap = {}
  x = 0
  y = 0
  cur = 1
  if (dim == 1):
    spiralMap[x] = {}
    spiralMap[x][y] = cur
  return spiralMap

res = createSpiral(1)
print('createSpiral result {}'.format(res))
print('0, 0 is ', res[0][0])