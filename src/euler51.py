import time 
from utils.mathHelpers import eratosthenes
from utils.mathHelpers import isPrime
print('project euler problem 51')
tic = time.perf_counter()

#read the file:
f = open("./resources/primesTo10000000.txt", "r")
asStr = f.read()
asList = asStr.split(',')
asIntList = [int(item) for item in asList]

# filter list down to items with repeats
def hasDupe(input):
  asStr = str(input)
  hasDupe = False
  countMap = {}
  for i in range(0, len(asStr)):
    countMap[asStr[i]] = 0
  for i in range(0, len(asStr)):
    countMap[asStr[i]] += 1
    if countMap[asStr[i]] > 1:
      hasDupe = True
  return hasDupe

noDupes = list(filter(hasDupe,asIntList))

""" f = open("./resources/nonDupesFiltered.txt", "x+")
f.write(",".join([str(elem) for elem in noDupes]))
f.close() """

toc = time.perf_counter()
print('finished in ', toc - tic)