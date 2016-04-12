#!/usr/bin/python
#Execute shell commands with python

import sys
import subprocess

COM=sys.argv[1]

p = subprocess.Popen(COM, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "Result of %s: %s" %(COM,output)
