print('project euler problem 44')

def getPentagonal(input):
  return input * (3 * input - 1)//2

first1000 = []
upperlim = 3000
for i in range(1, upperlim):
  first1000.append(getPentagonal(i))

print(first1000)

summed = first1000[3] + first1000[6] 

print("summed is ", summed)

print("summed in first", summed in first1000)

cands = []
for j in range(0, upperlim-2):
  for k in range(j, upperlim-1):
    su = first1000[j] + first1000[k]
    if su in first1000:
      diff = first1000[k] - first1000[j]
      if diff in first1000:
        print('cand found', diff, sum)
        cands.append(diff)

print('cands is ', cands)