print('project euler problem 34')

import math

def factOfDigs(input):
    asStr = str(input)
    factArr = []
    for char in asStr:
        print('char is ', char)
        factArr.append(math.factorial(int(char)))
    print('factArr is ', factArr)
    

for idx in range(0, 10):
    print('fact of Digs is ', factOfDigs(idx))
    print('{} factorial is {}'.format(idx, math.factorial(idx)))
