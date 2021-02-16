print('project euler problem 22')

def iterateNames(names):
        totalVal = 0
        for nameIdx in range(0, len(names)):
                name = names[nameIdx]
                nameVal = 0
                for ch in name:
                        val = ord(ch) - 64
                        nameVal += val
                totalVal += nameVal * (nameIdx + 1)
        print('totalVal', totalVal)

print("ordTest", ord('A'))
print("ordTest", ord('B'))
print("ordTest", ord('C'))          

reader = open('./resources/p022_names.txt')
try: 
  inputStr = reader.read()
  asArr = inputStr.split(",")
  processed = list(map(lambda x: x.replace('"', ''), asArr))
  processed.sort()
  iterateNames(processed)
finally:
  reader.close()

""" Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file? """