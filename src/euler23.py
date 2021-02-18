print('project euler problem 23')

def getDivisorsUnderN(n):
        divisors = []
        for i in range(1, int(n/2) + 1):
                if n % i == 0:
                        divisors.append(i)
        return divisors

def isAbundant(n):
        divisors = getDivisorsUnderN(n)
        sumOfDivisors = sum(divisors)
        return sumOfDivisors > n

upperBound = 28123
""" for i in range(1, upperBound):
        if isAbundant(i):
                abundants.append(i) """

# memoize the abundants


""" f = open("./resources/abundantsTo28123.txt", "x+")
f.write(",".join([str(elem) for elem in abundants]))
f.close() """

reader = open('./resources/abundantsTo28123.txt').read()

abundants = asArr = reader.split(',')
abundants = list(map(lambda x: int(x), asArr))
print('abundants ', abundants)

def isSumOfTwoAbundants(n):
        # for each item in asArr up to n, subtract and see if remainder is in array
        idx = 0
        subtractee = abundants[idx]
        while subtractee < n:
                diff = n - subtractee
                if diff in abundants:
                        return True
                idx += 1
                subtractee = abundants[idx]
        return False

notSummable = []
for i in range(1, upperBound):
        if not isSumOfTwoAbundants(i):
                notSummable.append(i)

print('notSummable', sum(notSummable))
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
 For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
 as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""