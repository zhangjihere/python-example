# -*- coding: utf-8 -*-
# python

import re

# match string using re.search
xx=re.search(r" (\w+@\w+\.com) ", "this xyz@example.com that")
if xx:
  print xx.group(1) 
else:
  print "no"

## replace using re.sub
myText = r"""<p><img src="./rabbits.gif" width="30" height="20">
and <img class="xyz" src="../cats.gif">,
but <img src ="tigers.gif">,
 <img src=
"bird.gif">!</p>"""
# using regex to replace the content, notice it contain captured pattern (the \1)
newText = re.sub(r'src\s*=\s*"([^"]+)\.gif"', r'src="\1.png"', myText)
print newText

## split string line using re.split
myText = ur"""你是我最苦澀的等待   |   you are my hardest wait
讓我歡喜又害怕未來   |   giving me joy and also fear the future"""
myLines=re.split(r'\n', myText)
for aLine in myLines:
  linesParts=re.split(r'\s*|\s*', aLine, re.U)
  print linesParts[0].encode('utf-8')

