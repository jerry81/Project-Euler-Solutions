print('project euler problem 34')

import math

def factOfDigs(input):
    asStr = str(input)
    factArr = []
    for char in asStr:
        if int(char) > input:
            return 0
        factArr.append(math.factorial(int(char)))
    return sum(factArr)
    
    
matches = []
for idx in range(0, 10000000):
    summed = factOfDigs(idx)
    if idx == summed:
        matches.append(idx)
    # print('idx is ', idx)
    # print('summed is ', summed)
print('matches is ', matches)
