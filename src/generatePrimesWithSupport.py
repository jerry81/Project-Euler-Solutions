from utils.mathHelpers import eratosthenesWithSupport
print('generating file')
res = eratosthenesWithSupport("./resources/primesTo20M.txt", 20000000, 30000000)

# res = eratosthenesWithSupport(filename, start, end)
# 10000 to 100000 primes
# find primes with repeated digits 

f = open("./resources/primesTo30M.txt", "x+")
f.write(",".join([str(elem) for elem in res]))
f.close()
