
print('generating file')

# 10000 to 100000 primes
# find primes with repeated digits 

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

f = open("./resources/2T_part1.txt", "r")
asStr = f.read()
lines = asStr.split('\n')
twoD = list(map(lambda line: line.split('\t'), lines))
flattened = []
for i in twoD:
    for j in i:
        flattened.append(j)
flattened = list(filter(lambda x: len(x) > 0, flattened))
# print('asList ', asList)
# filteredList = list(filter(lambda x: len(x) == 8, asList))
noDups = list(map(lambda x: int(x), flattened))
primeMap = {}
for i in range(len(noDups)):
  primeMap[noDups[i]] = True

""" f2 = open("./resources/largePrimeMap.txt", "x+")
f2.write(",".join([str(elem) for elem in noDups]))
f.close()
f2.close() """