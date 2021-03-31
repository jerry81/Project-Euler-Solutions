import time
from utils.mathHelpers import eratosthenes
from utils.mathHelpers import isPrime
from utils.fileUtils import openAndSplit
print('project euler problem 51')
tic = time.perf_counter()

# read the file:
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

# noDupes = list(filter(hasDupe,asIntList)) """


""" f = open("./resources/nonDupesFiltered.txt", "x+")
f.write(",".join([str(elem) for elem in noDupes]))
f.close() """

fiveDigitPrimes = list(filter(lambda x: len(str(x)) == 5, asIntList))

sixDigitPrimes = list(filter(lambda x: len(str(x)) == 6, asIntList))
""" sevDigitPrimes = list(filter(lambda x: len(str(x)) == 7, asIntList))
f = open("./resources/sevenDigitPrimes.txt", "x+")
f.write(",".join([str(elem) for elem in sevDigitPrimes]))
f.close()  """
f = open("./resources/sevenDigitPrimes.txt", "r")
asStr = f.read()
asList = asStr.split(',')
sevDigitPrimes = [int(item) for item in asList]
print('sev len is ', len(sevDigitPrimes))
# print('len is ', len(fiveDigitPrimes))
# print('len6 is ', len(sixDigitPrimes))

f = open("./resources/sevenDigitPrimes.txt", "r")

tento20 = openAndSplit('./resources/primesTo20M.txt')

tento20F = openAndSplit('./resources/primesNoDupes10Mto20M.txt')

raw = openAndSplit('./resources/eightDigPrimesUpTo179424673.txt')

print('len ten 2 20', len(tento20))
print('len filtered', len(tento20F))
print('len raw', len(raw))

tento30F = raw[100000: 200000] #first chunk

print('len 30', len(tento30F))

def getFamily(replacedDigits, baseNumber, maxNonPrimes):
    bnAsStr = list(str(baseNumber))
    nonPrimeCount = 0
    family = []
    if bnAsStr[replacedDigits[0]] != bnAsStr[replacedDigits[1]]:
        return family
    for i in range(0, 10):
        for dig in replacedDigits:
            bnAsStr[dig] = str(i)
        if not isPrime(int(''.join(bnAsStr))):
            nonPrimeCount += 1
            if nonPrimeCount > maxNonPrimes:
                return []
        else:
            family.append(int(''.join(bnAsStr)))
    return family


print("isPrime", not isPrime(86507))
# brute force:
# step thru each permutation of swapped indexes, index 1, index 2... index 1 and 2, index 1 and 3 ...
# fix some digits swap some digits.  then for each
# fixed number and idx pair, try 0-9 (10 ops), for each item that matches, add 1 to the count
# permutations of abcde - ab ac ad ae


def getPossibleReplacements(max):
    replacementIndexes = []
    for i in range(1, max):
        for j in range(i, max):
            newList = [i, j]
            replacementIndexes.append(newList)
    return replacementIndexes


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


""" cur = 10000000
while cur < 11000000:
  if not isPrime(cur):
    continue
  replacements = getPossibleReplacements(len(cur))
  for replacement in replacements: 
    family = getFamily(replacement, cur, 2)
    if (len(family) == 8):
        print("family is ", family)
  cur += 1 """

print('im done')
replacements = getPossibleReplacements(8)
print('replacements is ', replacements)
for pri in tento30F:
    for replacement in replacements:
        family = getFamily(replacement, pri, 2)
       # print('family possibility is ', family)
        if (len(family) == 8):
            print("family is ", family)


print('99991', isPrime(99991))
print('99989', isPrime(99989))

# repeats = makeRepeatIndexSet(fiveDigitPrimes)
# family = getFamily([2,3], 56003)
# filtered = list(filter(lambda item: isPrime(item), family))

""" replacements = getPossibleReplacements(7)
for pri in sevDigitPrimes:
    for replacement in replacements:
        family = getFamily(replacement, pri)
        if (len(family) == 8):
            print("family is ", family)
# print('five', fiveDigitPrimes)
toc = time.perf_counter()
print('finished in ', toc - tic) """
