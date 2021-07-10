from utils.annotations import track_performance

# sums of 5
# 1,4
# 2,3
# 1, sums of 4 - 1,3,1
  # 1, 2,2
# 2, sums of 3 - 2,1,1,1 
     # 2, 2, 1 - repeats with sums of 4
# 3, sums of 2 - 3,1,1 - repeats with sums of 4

# sums of 4
# 1, sums of 3 - 1,1,1
   # 1,1,2
# 2, sums of 2
  # 2, 1, 1 - repeat with sums of 3
# 3, 1
# 2, 2

# sums of 3
# 1, sums of 2 - 1,1,1
# 2, 1 

# sums of 2
# 1,1

@track_performance
def euler76():
    print('project euler problem 76')

# euler76()
