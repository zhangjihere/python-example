# -*- coding: utf-8 -*-
# python

# sort by custom order
import re

li = ['my283.jpg','my23i.jpg','web7-s.jpg','fris88large.jpg']
print li
# compare number inside string
def myComp(x, y):
  def getNum(str): return float(re.findall(r'\d+', str)[0])
  return cmp(getNum(x), getNum(y))

li.sort(myComp)
print li

# sort a matrix
mtx=[[2,6],[1,3],[5,4]]
print mtx
mtx.sort(key=lambda x:x[1]) # is equivalent to the following
# li.sort(lambda x, y: cmp(x[1], y[1]))
print mtx; # prints [[1, 3], [5, 4], [2, 6]]
