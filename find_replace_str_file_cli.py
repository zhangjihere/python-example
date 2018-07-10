#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

nn=len(sys.argv)

if nn !=5:
  print "Error: number of arguments does not match. Syntax should be: %s searchString repalceString inputFile outpuFile" % sys.argv[0]
else:
  searchStr=sys.argv[1]
  replaceStr=sys.argv[2]
  inputFile=open(sys.argv[3])
  outputFile=open(sys.argv[4], 'w')

  for thisLine in inputFile:
    outputFile.write(thisLine.replace(searchStr, replaceStr))

  outputFile.close()
  inputFile.close()



