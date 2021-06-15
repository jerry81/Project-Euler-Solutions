from utils.mathHelpers import getFactors
import json
from utils.toitientHelpers import o1isPrime

print('generating file')

# 10000 to 100000 primes
# find primes with repeated digits 

factorMap = {}
for i in range(2, 10):
    factors = []
    if o1isPrime(i):
        factors = []
    else:
        factors = list(set(getFactors(i)))
        factors.sort()
        factors.pop(0)
        factors.pop()
    factorMap[i] = factors
print('factorMap is ', factorMap)
    
# f = open("./resources/factorsTo1M.txt", "x+")
# json.dump(factorMap, f)
# f.close()
