#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re, shutil

inputDir=os.path.split(os.path.realpath(__file__))[0]; print 'Found'+inputDir
patternStr=ur'''<a href="(http[^"]+)">([^>]+)</a>'''
repStr=ur'''<a href="\1">\2↗</a>'''

def replaceStringInFile(filePath):
  "replaces all string by a regex substitution"
  tempName=filePath+'~~~'
  backupName=filePath+'~'
  inputFile=open(filePath)
  outputFile=open(tempName,'w')
  fContent=unicode(inputFile.read(), "utf-8")

  outText=re.sub(patternStr, repStr, fContent)

  outputFile.write((outText.encode("utf-8")))

  outputFile.close()
  inputFile.close()
  shutil.copy2(filePath, backupName)
  os.rename(tempName, filePath)  

  print "processed {}".format(filePath)

def fileFilter(dummyArg, thisDir, dirChildrenList):
  for thisChild in dirChildrenList:
    if '.txt' == os.path.splitext(thisChild)[1] and os.path.isfile(thisDir+'/'+thisChild):
      replaceStringInFile(thisDir+'/'+thisChild)

os.path.walk(inputDir, fileFilter, None)

