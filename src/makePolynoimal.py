from utils.fileUtils import writeMapToFile
print('generating file')


# 10000 to 100000 primes
# find primes with repeated digits 
def getXPolynomials(x, fun):
  output = {}
  for i in range(0, x):
    num = i + 1
    output[fun(num)] = True
  return output

def getSquare(n):
  return n**2

def getPentagon(n):
  return (n * (3*n - 1)) // 2

def getHex(n):
  return n * (2*n - 1)

def getHep(n):
  return (n * (5*n - 3)) // 2

def getOct(n):
  return n * (3*n - 2)

def getTri(n):
  return ((n * (n + 1))) // 2

squares = getXPolynomials(500, getSquare)
pentagonal = getXPolynomials(500, getPentagon)
hexa = getXPolynomials(500, getHex)
hep = getXPolynomials(500, getHep)
octa = getXPolynomials(500, getOct)
tri = getXPolynomials(500, getTri)

writeMapToFile('./resources/triangleMap.txt', tri)
writeMapToFile('./resources/squares.txt', squares)
writeMapToFile('./resources/pentagonal.txt', pentagonal)
writeMapToFile('./resources/hexa.txt', hexa)
writeMapToFile('./resources/hep.txt', hep)
writeMapToFile('./resources/octa.txt', octa)