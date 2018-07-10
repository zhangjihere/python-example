import os

def f1(xx, yy=[]):
  yy.append(xx)
  return yy

print f1(1)
print f1(1)
print f1(1)
print f1(3, [7, 8])
print f1(4)

print '#'*15

def f2(xx, yy=None):
  if yy is None:
    yy=[]
  yy.append(xx)
  return yy

print f2(1)
print f2(1)
print f2(1)
print f2(3, [7, 8])
print f2(4)

print os.path.realpath(__file__)

