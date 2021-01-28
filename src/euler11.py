print('project euler problem 11')

from utils.mathHelpers import getXTriangles, getFactors
import time

print(getFactors(20))
print(getXTriangles(20))
tic = time.perf_counter()
x = 0
triangles = getXTriangles(999999)
f = open("./resources/triangles.txt", "w")
f.write(",".join([str(elem) for elem in triangles]))
f.close() 
#read the file:
f = open("./resources/triangles.txt", "r")
asStr = f.read()
asList = asStr.split(',')
asIntList = [int(item) for item in asList]
print(76576500 in asIntList)
while True:
    if len(getFactors(asIntList[x])) >= 500:
        print(asIntList[x])
        print(len(getFactors(asIntList[x])))
        break
    x += 1
toc = time.perf_counter()
print("finished in ", toc - tic)