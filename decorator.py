# -*- coding: utf-8 -*-
# python

# http://www.xahlee.info/python/python_decorator.html
#########################################################
# example of decorator that check condition to decide whether to call

cc=True		# ← the condition
def gg1(f):
  """ a decorator for ff. If cc is true, run ff, else do nothing"""
  def hh(*arg, **kwargs): # ← param must catch all args of ff1
    """ do nothing function"""
    pass
  if cc:
    return f
  else:
    return hh

@gg1
def ff1(*args, **kwargs):
  # ff1 can be sending email, or any callable with no return value
  print "ff1"
  pass

ff1(3)
ff1(3, "Jane")
ff1(3, 4, k="thank you")
# if cc is true, then ff1 is called 3 times
# (different set arguments are used, to illustrate that our wrapper work well with them)
# if cc is false, Nothing's done, ff1 is not called.


#########################################################
# example of decorator with argument
# complex example, it means f=g(num)(f)(x)
def gg2(num):
  """a decorator for ff2. Ignore ff. Simply return num."""
  def h1(f):	# ← g(num)(f)
    def h2(x):  # ← g(num)(f)(x)
      return f(x)
    return h2
  return h1

@gg2(1)		# ← g(num)
def ff2(x):
  return repr(x) + " rabbits"

print ff2(1)
print ff2(2)
print ff2(3)

#########################################################

