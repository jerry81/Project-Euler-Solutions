print('project euler problem 33')

from utils.mathHelpers import reduceFraction

print('reduce fract 6 24', reduceFraction((6,24)))

def tryCancel(numer, denom):
    if numer % 10 == 0 and denom % 10 == 0:
        return None
    numerS = str(numer)
    denomS = str(denom)
    for i in range(0,2):
        for j in range(0,2):
            if numerS[i] == denomS[j]:
                numerS = numerS.replace(numerS[i], '', 1)
                denomS = denomS.replace(denomS[j], '', 1)
                return (numerS, denomS)
    return None


anomalies = []
for numer in range(10, 99):
    for denom in range(numer + 1, 100):
        quo = numer / denom
        cancelRes = tryCancel(numer, denom)
        if cancelRes == None or cancelRes[1] == '0':
            continue
        else: 
            cancelQuo = int(cancelRes[0]) / int(cancelRes[1])
            if (cancelQuo == quo):
                anomalies.append((numer, denom))

numProd = 1
denomProd = 1
for idx in range(0, len(anomalies)):
    numProd *= anomalies[idx][0]
    denomProd *= anomalies[idx][1]

print('reduced is ', reduceFraction((numProd, denomProd)))