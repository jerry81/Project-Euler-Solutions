from utils.annotations import track_performance

# naive, brute force
def getDigits(num):
  asStr = str(num)
  return len(asStr)

@track_performance
def euler63():
    print('project euler problem 63')
    baseLim = 1000
    powerLim = 100
    count = 0
    for base in range(0,baseLim):
      for e in range(0,powerLim):
        tested = base ** e 
        length = getDigits(tested)
        if (length == e):
          print('dig for base and exp is ', base, e, length)
          count += 1
    print('count is ', count)
    
euler63()
