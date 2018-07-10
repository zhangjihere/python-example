# -*- coding: utf-8 -*-
# python

# example of find/replace for all html files in a dir
# warning: this example does not deal with Unicode encoded files well

import os, sys, shutil

inputDir=os.path.split(os.path.realpath(__file__))[0];print inputDir
findStr=r"""Hello"""
repStr=r"""GoodBye"""

def replaceStringInFile(findStr, repStr, filePath):
  "replaces all findStr by repStr in file filepath"
  tempName=filePath+'~~'
  backupName=filePath+'~'
  inputFile=open(filePath)
  outputFile=open(tempName, 'w')

  for thisLine in inputFile:
    outputFile.write(thisLine.replace(findStr, repStr))

  outputFile.close()
  inputFile.close()
  shutil.copy2(filePath, backupName)
  os.rename(tempName, filePath)
  print "file processed: {}".format(filePath)

def filterFile(dummyArg, thisDir, dirChildrenList):
  for thisChild in dirChildrenList:
    if '.txt' == os.path.splitext(thisChild)[1] and os.path.isfile(thisDir+'/'+thisChild):
      replaceStringInFile(findStr, repStr, thisDir + '/' + thisChild)


os.path.walk(inputDir, filterFile, None)

