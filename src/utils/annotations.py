import time

def track_performance(decorated):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        decorated(*args, **kwargs)
        print('time taken is ', time.perf_counter() - tic)
    return wrapper