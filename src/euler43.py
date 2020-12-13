print('project euler problem 43')
from utils.mathHelpers import isPandigital, isPrime
from euler32 import getAllPerms, stringifyAndJoin

allPerms = [stringifyAndJoin(i) for i in getAllPerms([0,1,2,3,4,5,6,7,8,9])]
results = []
for x in allPerms:
  asStr = str(x)
  sub1 = int(asStr[1:4])
  sub2 = int(asStr[2:5])
  sub3 = int(asStr[3:6])
  sub4 = int(asStr[4:7])
  sub5 = int(asStr[5:8])
  sub6 = int(asStr[6:9])
  sub7 = int(asStr[7:10])
  if (sub1 % 2 != 0):
    continue
  if (sub2 % 3 != 0):
    continue
  if (sub3 % 5 != 0):
    continue
  if (sub4 % 7 != 0):
    continue
  if (sub5 % 11 != 0):
    continue
  if (sub6 % 13 != 0):
    continue
  if (sub7 % 17 != 0):
    continue
  results.append(x)

print("results is ", sum(results))

test1 = 12345667890
subStr1 = str(test1)[1:4]
print('substr1 is ', subStr1)