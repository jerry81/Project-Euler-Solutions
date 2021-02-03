print('project euler problem 16')
import time 

num = str(2**1000)
total = 0
for i in range(0, len(num)):
        curNum = int(num[i])
        total += curNum
tic = time.perf_counter()
print('answer: ', total)
print('took ', time.perf_counter() - tic)