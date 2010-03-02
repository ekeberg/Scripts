#!/usr/bin/env python

from pylab import *
import os
import re
import sys

if len(sys.argv) != 3:
    print "Usage: copy_good.py <last iteration number> <threshold>"
    sys.exit(1)
try:
    last_iteration = int(sys.argv[1])
except:
    print "Error: \"%s\" is not a valid iteration number" % sys.argv[1]
    sys.exit(1)
try:
    threshold = float(sys.argv[2])
except:
    print "Error \"%s\" is not a valid threshold" %sys.argv[2]
    sys.exit(1)


ls_out = os.popen('ls').readlines()

expr = re.compile('[0-9]{6}')
dirs = filter(expr.search,ls_out)
dirs = [d[:-1] for d in dirs]

for d in dirs:
    l = loadtxt("%s/uwrapc.log" % (d), skiprows=47)
    ferr = l[-1][3]

    if ferr < threshold:
        os.system("cp %s/real_space-%.7d.h5 final_good/%.3d.h5" % (d,last_iteration,int(d)))


