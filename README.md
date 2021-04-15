# Project Euler
greetings!  this repository is to both practice and learn python and to practice algorithms by working solutions to [project euler](https://projecteuler.net/) problems

required: python3
to run 
1.  cd src
2.  python3 <name of file> e.g. python3 ./euler33.py

# PythonLearning

## Definitions

PEP - python enhancement project 

First class object - has fuller range of functionality than other objects like primitive types

Tuple - an immutable list 

## Syntax

### Lists

list declared with []

listA[:] gets a copy of the list

listA[1:3] returns items 2 and 3 of the since the fourth item listA[3] is not included

listA[-1] gets last item in list

listA.extend vs listA.append 

extend deconstructs a list, append does not

listA.count("value") ''' returns # of occurences of "value" in listA '''

"value" in listA ''' returns True or False '''

listA.index("value")  ''' returns index of first occurence or raises exception if not found '''

### Tuple

declared with ()

faster than lists

### Set 

declared with {}

unique vals 

note that dictionaries are also declared with {}

can also be declared with set()

.add to append to set
.union to merge two sets

### Dictionary

Syntax like js objects

modify same as js notation 

empty dict false otherwise true 

access props with a["b"] syntax

### Fractions module 

import fractions // to import 

x = fractions.Fraction(1, 2) // 1/2

x * 2 // 2/2 

reduces automatically 

### None 

acts as the null value in python 

### OS module 

import os 

getcwd - get current working directory 

chdir - change directory 

### comprehension 

similar to js map 

apply function to each item in array 

[item * 2 for item in itemArray]

itemArray not effected ( creates a copy )

itemArray can be reassigned in place 

itemArray = [item * 2 for item in itemArray] works fine

### template strings 
'a is {}'.format(a)

### conversions
number to string 
str(123)
string to number 
int('123')

### shallow and deep copy
copy.copy(x)
copy.deepCopy(x)

### loop backwards
range(10, 0, -1) goes from 10 to 0 

### default args
def getNextState(coins, skip = False):

### misc
no ++ 
use +=
no function overloading


### block comment
triple quote

## arrays

### convert int array into string array
s = [str(i) for i in list]
### convert int to str 
d = 15
d.str()
### filter
filtered = filter(filterFn, originalArr)
#### gotchas 
+= doesn't work for pushing dictionaries, use .append

## strings

### replace in str x number of times
s = 'abababab'
print(s.replace('a', 'A', 2)) 
#result AbAbabab

### join 
joins all items in iterable and appends to string
e.g. "".join(items)

python also has a split method for going the other direction

## math 

### division
floor division //
decimal division /

## file

### reading file example 

reader = open('./resources/p042_words.txt')
try: 
  inputStr = reader.read()
  print('inputStr', inputStr)
finally:
  reader.close()

### loops
break and continue both supported

### lambda with filter

filter(lambda x: x % 2 == 0, arr)

### different assignments

(x_train, y_train), (x_test, y_test) = mnist.load_data() 
two tuples separated by comma - this is known as sequence assignment 
e.g.
a, b, c = 'HEY'
a gets H, b gets E, c gets Y

### using *args and **kwargs

allow a function to accept arbitrary number of positional and keyword args

def arbiraryInput(*args, **kwargs):
  for arg in args:
    print('arg', arg)
  for key, val in kwargs.items():
    print(f"key is {key} val is {val}")
  
### decorator with args