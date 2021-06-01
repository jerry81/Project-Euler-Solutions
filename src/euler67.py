from utils.annotations import track_performance
from utils.fileUtils import openAndSplitPlus

@track_performance
def euler67():
    triangleLines = openAndSplitPlus('./resources/p067_triangle.txt', '\n')
    noEmpty = list(filter(lambda x: len(x) > 0, triangleLines))
    asArr = list(map(lambda x: x.split(' '), noEmpty))
    print('project euler problem 67')


euler67()