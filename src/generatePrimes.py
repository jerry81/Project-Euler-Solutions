from utils.mathHelpers import eratosthenes
print('generating file')
res = eratosthenes(100000000)

# 10000 to 100000 primes
# find primes with repeated digits 

f = open("./resources/primesTo100000000.txt", "x+")
f.write(",".join([str(elem) for elem in res]))
f.close()
