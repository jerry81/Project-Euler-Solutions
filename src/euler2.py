print('project euler problem 2')

def isEven(input):
  return input % 2 == 0

def fib(termIdx):
  if termIdx == 0:
    return 1
  if termIdx == 1:
    return 2
  return fib(termIdx - 1) + fib(termIdx - 2)

def getFibSeq(upTo):
  returned = [1, 2]
  idx = 2
  while True:
    nextTerm = returned[idx-1] + returned[idx-2]
    if nextTerm > upTo:
      break
    returned.append(nextTerm)
    idx+=1
  return returned

print('get fib seq to 10', getFibSeq(4000000))
print('sum of evens is ', sum(list(filter(lambda x: isEven(x), getFibSeq(4000000)))))