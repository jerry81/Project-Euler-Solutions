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
