print('project euler problem 18')
import time 
raw = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# 0, 0, 0, 0... 0
# 0, 0, 0, 0 ... 1
# 0, 0, 0, 1, 0

# recursive solution to get all paths 
def getPaths(level, rawArr):
        currentLevel = rawArr[level]
        if len(rawArr) <= level + 1:
                return [[x] for x in range(0,len(currentLevel))]
        nextLevel = getPaths(level+1, rawArr)
        for i in range(0, len(nextLevel)):
                curArr = nextLevel[i].copy()
                lastItem = curArr[-1]
                # add self
                if lastItem < (len(currentLevel)):
                        nextLevel[i].append(lastItem)
                if lastItem - 1 >= 0:
                        copy2 = curArr.copy()
                        copy2.append(lastItem -1)
                        nextLevel.append(copy2)
                # add -1 and +1 if within bounds
                #if lastItem - 2 >= 0:
                #        copy1 = curArr.copy()
                #        copy1.append(lastItem - 2)
                #        nextLevel.append(copy1)
        return nextLevel
tic = time.perf_counter()
rawArr = raw.split("\n")
for i in range(0, len(rawArr)):
        numStr = rawArr[i]
        rawArr[i] = [int(x) for x in numStr.split(' ')]
print('rawArr', rawArr)
paths = getPaths(0, rawArr)
maxNum = 0
pathIdx = 0
refinedPaths = list(filter(lambda x: len(x) == 15, paths))
print('paths is ', refinedPaths)
for i in range(0, len(refinedPaths)):
        path = refinedPaths[i]
        path.reverse()
        total = 0
        for j in range(0, len(path)):
                cur = path[j]
                row = rawArr[j]
                total += row[cur]
        if total > maxNum:
                maxNum = total
                pathIdx = path


print('max is ', maxNum)
print('path is ', pathIdx)
print('took ', time.perf_counter() - tic)

# [0, 0], [0,1], [1, 1], [2,1], [1,2], [2, 2], [3,2] ...
# [0, 0, 0], [0,0,1], [0,1,0], [0,1,1], [0,1,2], [1, 1, 0], [1,1]
# or 
# [0]
# [0, 0], [0,1]
# [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 2]