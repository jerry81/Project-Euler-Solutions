print('project euler problem 21')
import time 


tic = time.perf_counter()
def getSumOfDivisorsUnderN(n):
        arr = []
        for i in range(1, int(n/2) + 1):
                if n % i == 0:
                        arr.append(i)
        return sum(arr)

print('220', getSumOfDivisorsUnderN(220))
print('284', getSumOfDivisorsUnderN(284))

allD = {}

upperLim = 10000
for i in range(1, upperLim):
        allD[str(i)] = getSumOfDivisorsUnderN(i)

print('allD is ', allD)

amicables = set()
for key in allD:
        currentSum = allD[key]
        if currentSum >= 1 and currentSum < upperLim:
                potentialPairIdx = str(currentSum)
                potentialPair = allD[potentialPairIdx]
                if str(potentialPair) == key and int(key) != currentSum:
                        amicables.add(int(currentSum))
                        amicables.add(int(key))


print('amicaables', amicables)
print(sum(amicables))

print('time took', time.perf_counter() - tic)

""" Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. """