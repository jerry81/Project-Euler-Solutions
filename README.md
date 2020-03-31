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

### Dictionary

Syntax like js objects

modify same as js notation 

empty dict false otherwise true 

### Fractions module 

import fractions // to import 

x = fractions.Fraction(1, 2) // 1/2

x * 2 // 2/2 

reduces automatically 

### None 

acts as the null value in python 