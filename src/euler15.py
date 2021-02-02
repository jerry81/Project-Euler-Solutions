print('project euler problem 15')
import time 

def getPaths(x, y, maxI):
        if (x >= maxI and y >= maxI):
                return 0
        if (x >= maxI):
                return 1
        if (y >= maxI):
                return 1
        return getPaths(x + 1, y, maxI) + getPaths(x, y + 1, maxI)

tic = time.perf_counter()
# print('2', getPaths(0, 0, 20))


def getNextPathArr(lastArr):
        nextArr = [1]
        for i in range(1, len(lastArr)):
                nextArr.append(nextArr[i-1]+lastArr[i])
        print(nextArr)

        nextArr.append(nextArr[len(nextArr) - 1] * 2)
        return nextArr
        

#optimization

# only need one side 

# get array of values for one side
# e.g. 6 3 1

# get array of values for next iteration 

# 20 10 4 1

# 70 35 15 5 1
print(getNextPathArr([]))
nextArr = []
for j in range(0, 19):
        nextArr = getNextPathArr(nextArr)
print(getNextPathArr(nextArr))
print('took ', time.perf_counter() - tic)