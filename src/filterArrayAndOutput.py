
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

f = open("./resources/primesTo20M.txt", "r")
asStr = f.read()
asList = asStr.split(',')
filteredList = list(filter(lambda x: len(x) == 8, asList))
noDups = list(filter(lambda x: hasDupe(int(x)),filteredList))

f2 = open("./resources/primesNoDupes10Mto20M.txt", "x+")
f2.write(",".join([str(elem) for elem in noDups]))
f.close()
f2.close()