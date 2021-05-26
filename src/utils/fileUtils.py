import json

def openAndSplitPlus(filename, separator):
    f = open(filename, "r")
    asStr = f.read()
    asList = asStr.split(separator)
    return asList  

def openAndSplit(filename):
    return openAndSplitPlus(filename, ',')

def writeMapToFile(filename, arr):
  f = open(filename, "w")
  f.write(json.dumps(arr))
  f.close() 

def writeArrayToFile(filename, arr):
  f = open(filename, "w")
  asStrs = map(lambda x: str(x), arr)
  f.write(",".join(asStrs))
  f.close() 

def openMap(filename):
  f = open(filename, 'r')
  return json.loads(f.read())