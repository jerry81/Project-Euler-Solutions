import functools


def my_dec(decorated):
    def wrapper(*args, **kwargs):
        print('pre')
        decorated(*args, **kwargs)
        print('post')
    return wrapper


@my_dec
def hello():
    print('hello no arg')


@my_dec
def hello2(item):
    print('hello with item', item)


@my_dec
def helloWithMixed(item, kw1, kw2):
    print("fixed is ", item)
    print("kw1 is ", kw1)
    print("kw2 is ", kw2)


hello()
hello2("world")
helloWithMixed("fixed", kw2="kw2", kw1="kw1")

# example of decorating with return value


def my_dec2(fn):
    @functools.wraps(fn)  # lets fn keep its introspection info
    def wrapper(*arg, **args):
        print('pre')
        returned = fn(*arg, **args)
        print('post')
        return returned
    return wrapper


@my_dec2
def helloWithReturn(num):
    print('working it arg is ', num)
    return num+1


result = helloWithReturn(2)
print("result is ", result)

def dec_nested(notFunction): # this syntax is specific to decorators that take in params
  def outer(fn):
    def inner():
      print('PRE with arg', notFunction)
      fn()
      print('POST')
    return inner
  return outer

@dec_nested("dec arg!")
def helloNest():
  print('hello nested')

helloNest()

# issubclass example
class Polygon:
  def __init__(polygonType):
    print('Polygon is ', polygonType)

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__('triangle')

print(issubclass(Triangle, Polygon))
# second arg can be a tuple
print(issubclass(Triangle, (Polygon, bool)))

# contextmanager example

from contextlib import contextmanager 
import time

@contextmanager
def managed():
  time.sleep(1) # sleeps 3 seconds
  try:
    yield 'hello world'
  finally:
    print('released')

with managed() as mg:
  print('mg is ', mg)
  time.sleep(1)

print('done with')

# zip

iter1 = [1,2,3]
zip1 = zip(iter1)
print('zip1', list(zip1))

iter2 = ['a', 'b', 'c']

zip2 = zip(iter2, iter1)

print('zip2', list(zip2))

print('this doesnt work', dict(zip2)) # because zip2 has already been converted to list
print('asdict', dict(zip(iter2, iter1))) # this works