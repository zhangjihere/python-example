#!/usr/bin/env python
# -*- coding:utf-8 -*-

# example, find and replace string in file based on Unicode

import os, shutil

inputDir=os.path.split(os.path.realpath(__file__))[0]; print "Found {}".format(inputDir)

findReplacePairs = [
(u"西游记", u"西游记 Monkey King"),
# more pair here
]

def replaceStringInFile(fname):
  print fname
  backupFile=fname+'~'
  inputFile=fname
  outputFile=fname+'~~'

  inF=open(inputFile, 'r')
  fcontent= unicode(inF.read(), 'utf-8')
  inF.close()

  for str in findReplacePairs:
    outContent=fcontent.replace(str[0], str[1])
  
  outF=open(outputFile, "wb")
  outF.write(outContent.encode("utf-8"))
  outF.close() 

  shutil.copy2(fname, backupFile)
  os.rename(outputFile, fname)

if __name__=='__main__':
  for cur_dir, subdirs, subfiles in os.walk(inputDir):
    for subfile in subfiles:
      extn=os.path.splitext(subfile)[1]
      fname=cur_dir+'/'+subfile
      if '.txt' == extn and os.path.isfile(fname):
        replaceStringInFile(fname) 
