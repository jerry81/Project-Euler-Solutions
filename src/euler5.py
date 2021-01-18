print('project euler problem 5')
import time 
tic = time.perf_counter()
test = 1
while True:
  passes = True
  for i in range(1, 21):
    if test % i != 0:
      passes = False
      break
  if passes == True:
    print('sol is ', test)
    break
  test += 1
toc = time.perf_counter()

print('total time is ', toc - tic)