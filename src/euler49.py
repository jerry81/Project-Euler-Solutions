from utils.mathHelpers import isPrime
print('project euler problem 49')

def isPerm(src, tgt):
  srcs = str(src)
  tgts = str(tgt)

  if src == tgt:
    return False
  if len(srcs) != len(tgts):
    return False

  for ch in srcs:
    if (srcs.count(ch) != tgts.count(ch)):
      return False
  
  return True

print('isPerm', isPerm(123, 312))

print('isPerm2', isPerm(1487, 4817))

print('isPerm3', isPerm(4817, 8147))

print('isPerm4', isPerm(213, 512))

print ('isPerm5', isPerm(6733, 6673))


for starting in range(100, 10000):
  if (not isPrime(starting)):
    continue
  for incr in range(0, 3335):
    for i in range(1, 3):
      curr = starting + (i * incr)
      if (not isPrime(curr)):
        break
      if (not isPerm(curr, starting)):
        break
      if (i == 2):
        print('curr is ', curr)
        print('starting is ', starting)
        print('incr is ', incr)
