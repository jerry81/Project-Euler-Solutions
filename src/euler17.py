print('project euler problem 17')
import time 

# one two ... ten 
# eleven twelve thirteen .. twenty
# twenty-one twenty-nine
# thirty-one thrity-nine
# forty
# one hundred and ...
# two hundred and ...

numberMap = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
}
total = 0
finalTotal=0
miniTest = 0
for i in range(1, 6):
  miniTest+=len(numberMap[i])
for i in range(1, 21):
  total+=len(numberMap[i])
for i in range(21, 100):
        tens = int(str(i)[0])*10
        singles = int(str(i)[1])
        numAsStr = '{}{}'.format(numberMap[tens], numberMap[singles])
        print('numasstr', numAsStr)
        total+=len(numAsStr)
finalTotal += total

for j in range(1, 10):
        finalTotal += (len(numberMap[100]) + len('and') + len(numberMap[j]))*99 + total # onehundredand * 99 + (total from 1 to 99)
        finalTotal += len(numberMap[100]) + len(numberMap[j]) # onehundred, twohundred, etc...
finalTotal += len(numberMap[1000]) + len(numberMap[1]) # oneThousand
print("total is ", total)    
print("ftotal is ", finalTotal)
print('minitest is ', miniTest)
tic = time.perf_counter()
print('took ', time.perf_counter() - tic)