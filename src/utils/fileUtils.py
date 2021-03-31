def openAndSplit(filename):
    f = open(filename, "r")
    asStr = f.read()
    asList = asStr.split(',')
    return asList
