print('project euler problem 30')

max = 354294

def getPowerArray(input, power):
  ret = []
  stringified = str(input)
  for digit in stringified:
    asNumber = int(digit)
    powered = asNumber**power
    ret.append(powered)
  return ret 


cur = 2
sums = []
while cur < max: 
  res = getPowerArray(cur, 5)
  resSum = sum(res)
  if (cur == resSum):
    print('{} and {} are equal'.format(cur, resSum))
    sums.append(cur)
  cur += 1
print('sums is {}'.format(sums))
print('sum of sums is {}'.format(sum(sums)))
