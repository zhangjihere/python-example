#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

# split path into dir part, file part
print '#'*10 + 'split'
print os.path.split("/home/aa/bb/ff.html")	# ('/home/aa/bb', 'ff.html')


# get dir part
print '#'*10 + 'dirname'
print os.path.dirname("/home/aa/bb/ff.html")	# /home/aa/bb

# get file name part of a path
print '#'*10 + 'basename'
print os.path.basename("/home/aa/bb/ff.html")	# ff.html

# get file extension
print '#'*10 + 'splitext'
st=os.path.splitext("/home/aa/bb/ff.html")	# ('/home/aa/bb/ff', '.html')
print st[0]
print st[1]

# check if file exists
print '#'*10 + 'exists'
print os.path.exists("/home/")			# True
print os.path.exists("/home/9572")		# False

# compute relative path
print '#'*10 + 'relpath'
print os.path.relpath("/home/aa/bb/ff.html", "/home/aa") # bb/ff.html

# get absolute path
fp="/usr/bin/../bin/vi"
# remove redundant ../
print '#'*10 + 'normalized'
print os.path.normpath(fp)

# similar to os.path.normpath(fp) but does a bit more
print '#'*10 + 'abspath'
print os.path.abspath(fp)

# resolve symbolic link
print '#'*10 + 'realpath', "/usr/bin/sh -> /usr/bin/bash"
print os.path.realpath("/usr/bin/sh")		# /usr/bin/vim.basic
print os.path.realpath("/usr/bin/../bin/sh")	# /usr/bin/vim.basic


