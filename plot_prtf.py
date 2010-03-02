#! /usr/bin/python

import sys
sys.path.append("/home/ekeberg/Scripts")
from plot_2d import *

def plot_prtf():
    data = plot_2d()
    pylab.plot([data[0,0],data[0,-1]],[pylab.exp(-1),pylab.exp(-1)])

    for i in range(len(data[1,:])):
        if data[1,i] < pylab.exp(-1):
            break
    pylab.plot([data[0,i],data[0,i]],[0,pylab.exp(-1)])

if __name__ == "__main__":
    plot_prtf()
    pylab.show()

