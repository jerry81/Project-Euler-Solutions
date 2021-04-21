from utils.annotations import track_performance
print('project euler problem 52')


def populateMap(input, inMap):
    for c in input:
        try:
            inMap[c] += 1
        except:
            inMap[c] = 1

def checkSameDigits(a, b):
    aS = str(a)
    bS = str(b)
    if (len(aS) != len(bS)):
        return False
    aM = {}
    bM = {}
    populateMap(aS, aM)
    populateMap(bS, bM)
    for key, value in aM.items():
        try:
            if bM[key] != value:
                return False
        except:
            return False
    return True

def getInputArr(seed):
    arr = []
    for i in range(6):
        arr.append(seed * (i + 1))
    return arr

@track_performance
def euler52():
    print('check 251748, 125874', checkSameDigits(251748, 125874))
    tryout = 10
    while True: 
        input = getInputArr(tryout)
        first = input[0]
        found = True
        for i in range(1, len(input)):
            cur = input[i]
            if not checkSameDigits(first, cur):
                found = False
                break
        if found:
            print('first is ', first)
            return                        
        tryout += 1
        
euler52()
