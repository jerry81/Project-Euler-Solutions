print('project euler problem 20')

def getFactoral(n):
        total = 1
        for i in range(n, 0, -1):
                total*=i
        return total

fact100 = getFactoral(100)

asStr = str(fact100)

summ = 0
for chIdx in range(0, len(asStr)):
        asInt = int(asStr[chIdx])
        summ += asInt

print('sum is ', summ)

""" n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100! """