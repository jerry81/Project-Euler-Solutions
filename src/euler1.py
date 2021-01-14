print('project euler problem 1')

def getMultiplesOf3And5(count):
  returned = []
  for i in range(0, count):
    if i % 3 == 0 or i % 5 == 0:
      returned.append(i)
  return returned

print(sum(getMultiplesOf3And5(1000)))

