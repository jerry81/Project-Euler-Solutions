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