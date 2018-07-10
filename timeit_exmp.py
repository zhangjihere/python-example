#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example of using timeit.timeit
# testing the speed of a function that takes one argument

mydata=5
def f1(x):
  return x+1


if __name__ == '__main__':
  import timeit

  t=timeit.timeit("f1(mydata)", setup="from __main__ import f1, mydata", number=5000000)
  print "time elapse is %0.5s\n"%t


