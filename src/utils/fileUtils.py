def openAndSplitPlus(filename, separator):
    f = open(filename, "r")
    asStr = f.read()
    asList = asStr.split(separator)
    return asList  

def openAndSplit(filename):
    return openAndSplitPlus(filename, ',')