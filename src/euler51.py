import time 
from utils.mathHelpers import eratosthenes
print('project euler problem 51')
tic = time.perf_counter()

#read the file:
f = open("./resources/primesTo10000000.txt", "r")
asStr = f.read()
asList = asStr.split(',')
asIntList = [int(item) for item in asList]
print(asIntList)
toc = time.perf_counter()
print('finished in ', toc - tic)