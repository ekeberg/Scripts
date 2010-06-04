#! /usr/bin/python

import sys
import pylab

def plot_1d():
    if len(sys.argv) < 2:
        print "Need at least one data set"
        sys.exit(1)

    fig = pylab.figure(1)
    ax = fig.add_subplot(111)

    for f in sys.argv[1:]:
        try:
            data = pylab.loadtxt(f)
        except:
            print "Error %s is not a readable file.\n" % (f)
            sys.exit(1)

        #data = pylab.transpose(data)

        ax.plot(data,label=f)

    if len(sys.argv) > 2:
        ax.legend()

    return data

if __name__ == "__main__":
    plot_1d()
    pylab.show()
