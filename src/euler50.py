from utils.mathHelpers import isPrime
print('project euler problem 50')

primesToOneM = []
for i in range(1, 1000001):
  if (isPrime(i)):
    primesToOneM.append(i)

print(primesToOneM)

print('len is ', len(primesToOneM))

print(sum(primesToOneM[3:546]))

longestSplit = 0
lower = 0
upper = 0
for i in range(0, 1000):
  print('i is now ', i)
  for j in range(1, 1000):
    if (j - i < longestSplit):
      continue
    curSum = sum(primesToOneM[i:j])
    print('curSum is ', curSum)
    if curSum in primesToOneM:
      split = j - i
      if (split > longestSplit):
        lower = i
        upper = j
        longestSplit = split

print('longestSplit', longestSplit)
print('lower', lower)
print('upper', upper) 