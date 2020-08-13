print('project euler problem 34')

import math

def factOfDigs(input):
    asStr = str(input)
    factArr = []
    for char in asStr:
        print('char is ', char)
        factArr.append(math.factorial(int(char)))
    return sum(factArr)
    
    

for idx in range(0, 20):
    print('idx {} fact of Digs is {}'.format(idx, factOfDigs(idx)))
