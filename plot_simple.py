#! /usr/bin/python

import sys
import pylab

if len(sys.argv) != 2:
    print "Need a data set"
    sys.exit(1)
try:
    data = pylab.loadtxt(sys.argv[1])
except:
    print "Error %s is not a readable file.\n" % (sys.argv[1])
    sys.exit(1)


for i in pylab.transpose(data):
    pylab.plot(i)

pylab.show()
