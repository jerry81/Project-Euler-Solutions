from utils.annotations import track_performance

def getNForDCloseTo3over7(d):
    return (3 * d) // 7

@track_performance
def euler71():
    print('project euler problem 71')

euler71()