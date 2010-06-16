#! /usr/bin/python

import sys
sys.path.append("/home/ekeberg/Scripts")
from plot_2d import *

def plot_prtf(in_file):
    data = read_2d(in_file)
    pylab.plot([data[0,0],data[0,-1]],[pylab.exp(-1),pylab.exp(-1)])

    for i in range(len(data[1,:])):
        if data[1,i] < pylab.exp(-1):
            break
    pylab.plot([data[0,i],data[0,i]],[0,pylab.exp(-1)])

if __name__ == "__main__":
    try:
        plot_prtf(sys.argv[1])
        pylab.show()
    except:
        print """
Usage: plot_prtf <prtf_file>

