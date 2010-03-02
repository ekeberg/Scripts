#!/usr/bin/env python

import os
import re
import sys

if len(sys.argv) != 2:
    print "Usage: copy_final.py <last iteration number>"
    sys.exit(1)
try:
    last_iteration = int(sys.argv[1])
except:
    print "Error: \"%s\" is not a valid iteration number" % sys.argv[1]
    sys.exit(1);

l = os.popen('ls').readlines()

expr = re.compile('[0-9]{6}')
dirs = filter(expr.search,l)
dirs = [d[:-1] for d in dirs]

for d in dirs:
    os.system("cp %s/real_space-%.7d.h5 final_real/%.3d.h5" % (d,last_iteration,int(d)))
