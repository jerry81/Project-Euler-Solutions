print('project euler problem 10')

_2M = 2000000

reader = open('./resources/primesTo10000000.txt')

inputStr = reader.read()
filtered = list(map(lambda x: int(x), inputStr.split(',')))

x = 0
total = 0
nextPrime = filtered[x]
while nextPrime < _2M:
    total += nextPrime
    x += 1
    nextPrime = filtered[x]
print('total', total)