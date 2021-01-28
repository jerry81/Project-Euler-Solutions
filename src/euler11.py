print('project euler problem 11')

from utils.mathHelpers import getXTriangles, getFactors
import time

print(getFactors(20))
print(getXTriangles(20))
tic = time.perf_counter()
x = 0
triangles = getXTriangles(999999)
f = open("./resources/triangles.txt", "x+")
f.write(",".join([str(elem) for elem in triangles]))
f.close() 
""" while True:
    if len(getFactors(triangles[x])) == 500:
        print(x)
        break
    x += 1
toc = time.perf_counter()
print("finished in ", toc - tic) """