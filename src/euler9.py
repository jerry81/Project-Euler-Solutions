print('project euler problem 9')
from math import sqrt

for i in range(1, 2000):
    for j in range(1, 2000):
        c = i**2 + j**2
        if sqrt(c) == int(sqrt(c)):
            if i + j + sqrt(c) == 1000:
                print(i*j*sqrt(c))