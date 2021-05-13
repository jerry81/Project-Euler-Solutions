from utils.myitertools import getAllPerms
print('project euler problem 32')

firstPerm = [1,2,3,4,5,6,7,8,9]
allPerms = getAllPerms(firstPerm)

def stringifyAndJoin(arr):
  s = [str(i) for i in arr]
  return int("".join(s))

print('strngifyandjoin [1,2,3]', stringifyAndJoin([1,2,3]))

summed = 0
products = set()
for x in range(0, len(allPerms)):
  # = [5:10]
  perm = allPerms[x]
  product = stringifyAndJoin(perm[5:10])
  
  # try [0:1]*[1:5]
  operand1 = stringifyAndJoin(perm[0:1])
  operand2 = stringifyAndJoin(perm[1:5])
  triedProduct = operand1 * operand2
  if triedProduct == product:
    print('hit', product, operand1, operand2)
    products.add(product)

  # try [0:2] * [2:5]
  operand3 = stringifyAndJoin(perm[0:2])
  operand4 = stringifyAndJoin(perm[2:5])
  triedProduct2 = operand3 * operand4
  if triedProduct2 == product:
    print('hit', triedProduct2, operand3, operand4)
    products.add(product)

for prod in products:
  summed += prod

print('all perms has {} items'.format(len(allPerms)))
print('summed is ', summed)