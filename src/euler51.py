import time 
from utils.mathHelpers import eratosthenes
from utils.mathHelpers import isPrime
print('project euler problem 51')
tic = time.perf_counter()

#read the file:
f = open("./resources/nonDupesFiltered.txt", "r")
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

""" noDupes = list(filter(hasDupe,asIntList)) """

""" f = open("./resources/nonDupesFiltered.txt", "x+")
f.write(",".join([str(elem) for elem in noDupes]))
f.close() """

fiveDigitPrimes = list(filter(lambda x: len(str(x)) == 5,asIntList))
sixDigitPrimes = list(filter(lambda x: len(str(x)) == 6,asIntList))
print('len is ', len(fiveDigitPrimes))
print('len6 is ', len(sixDigitPrimes))

# brute force: 
# step thru each permutation of swapped indexes, index 1, index 2... index 1 and 2, index 1 and 3 ... 
# fix some digits swap some digits.  then for each 
# fixed number and idx pair, try 0-9 (10 ops), for each item that matches, add 1 to the count
# permutations of abcde - ab ac ad ae

def makeRepeatIndexSet(inputArr):
  repeats = set()
  for i in range(0, len(inputArr)):
    repeat = []
    cur = str(inputArr[i])
    for j in range(0, len(cur)):
      for k in range(j, len(cur)):
        if cur[j] == cur[k]: 
          repeat.append(j)
          repeat.append(k)
      repeats.add(tuple((set(repeat))))
  return repeats
    
print('99991', isPrime(99991))
print('99989', isPrime(99989))

repeats = makeRepeatIndexSet(fiveDigitPrimes)
print('repeats are ', repeats)
# print('five', fiveDigitPrimes)
toc = time.perf_counter()
print('finished in ', toc - tic)