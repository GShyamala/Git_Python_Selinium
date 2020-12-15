import array as arr

from urllib3.connectionpool import xrange

a=arr.array('u',['a','r','w','v','d'])
b=arr.array('i',[1,4,5,6])
print(a)
print(b[::-1])
a=range(1,10)
b=xrange()(1,10)
print(type(a))
print(type(b))
print(a)
print(b)

