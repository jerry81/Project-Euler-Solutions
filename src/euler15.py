print('project euler problem 15')

def getPaths(x, y, maxI):
        if (x >= maxI and y >= maxI):
                print('returning 0')
                return 0
        if (x >= maxI):
                print('calling ', x, y, maxI)
                return 1 + getPaths(x, (y + 1), maxI)
        if (y >= maxI):
                return 1 + getPaths((x + 1), y, maxI)
        print('returning default')
        return getPaths(x + 1, y, maxI) + getPaths(x, y + 1, maxI)

print('2', getPaths(0, 0, 2))