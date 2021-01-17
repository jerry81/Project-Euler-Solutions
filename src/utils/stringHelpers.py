def isPalindrome(asStr): 
    for idx in range(0, len(asStr)):
      # compare first and last 
      first = idx
      last = len(asStr) - idx - 1
      if first >= last:
          return True
      firstVal = asStr[first]
      lastVal = asStr[last]
      if firstVal != lastVal:
          return False