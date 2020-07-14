print('project euler problem 30')

sampleNumber = 3456

def getFourthPowerArray(input):
  ret = []
  stringified = str(input)
  for digit in stringified:
    asNumber = int(digit)
    powered = asNumber**4
    ret.append(powered)
  return ret 

res = getFourthPowerArray(sampleNumber)


print('res is {}'.format(res))
print('sum is {}'.format(sum(res)))