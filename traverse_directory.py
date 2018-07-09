# -*- coding: utf-8 -*-
# python

# traverse a dir, and list only html files

import os, pprint

mydir='/home/zhangji/projects_repo/python-demo/first_step_python'
result_list=[]


def processThisFile(fpath):
  print 'get touched', fpath
  result_list.append(fpath)


def filterFile(thisDir, dirChildrenList):
  for f in dirChildrenList:
    print "  %s" % f
    if ".txt" == os.path.splitext(f)[1] and os.path.isfile(thisDir+"/"+f):
      processThisFile(os.path.join(thisDir, f))

  
for dir_path, subdir_list, file_list in os.walk(mydir):
  print "Found dir_path: %s" % dir_path
  filterFile(dir_path, file_list)
  
print
pprint.pprint(result_list)



