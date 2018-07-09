# -*- coding: utf-8 -*-
# python

# example of getting environment variable


import os
from pprint import pprint

pprint(os.getenv("HOME", "default value if none"))

#pprint(os.environ)
for e_key, e_val in os.environ.iteritems():
  if e_key=="HTTPS_PROXY":
    pprint(e_key+":"+e_val)



