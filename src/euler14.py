print('project euler problem 14')

def nextCollatz(input):
    if (input % 2) == 0:
        # even 
        return input // 2
    else:
        # odd
        return (3 * input) + 1

def getSeries(input):
    series = []
    while (input != 1):
        series.append(input)
        input = nextCollatz(input)
    
    series.append(1)
    return series

max = 0
maxI = 0
for i in range(13, 1000000):
    cur = len(getSeries(i))
    if cur > max:
        max = cur 
        maxI = i

print('maxI is ', maxI)