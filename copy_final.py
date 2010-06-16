#!/usr/bin/env python

import os
import re
import sys

def copy_final(final):
    if len(arguments) != 1:
        print "Usage: copy_final.py <last iteration number>"
        sys.exit(1)
    try:
        last_iteration = final
    except:
        print "Error: \"%s\" is not a valid iteration number" % final
        sys.exit(1);

    l = os.popen('ls').readlines()

    expr = re.compile('[0-9]{6}')
    dirs = filter(expr.search,l)
    dirs = [d[:-1] for d in dirs]

    for d in dirs:
        os.system("cp %s/real_space-%.7d.h5 final_real/%.3d.h5" % (d,last_iteration,int(d)))

if __name__ == "__main__":
    try:
        copy_final(int(sys.argv[1:]))
    except:
        print "Usage: copy_final <last iteration number>"
