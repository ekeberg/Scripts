#! /usr/bin/python

import spimage, pylab, sys

if len(sys.argv) <= 1:
    print """
Usage:  python_script_image_to_png <image_in.h5> <image_out.h5> [colorscale]

Colorscales:
Jet
Gray
PosNeg
InvertedPosNeg
Phase
InvertedPhase
Log (can be combined with the others)
Shift (can be combined with the others)

"""
    exit(1)

try:
    img = spimage.sp_image_read(sys.argv[1],0)
except:
    print "Error: %s is not a readable .h5 file\n" % sys.argv[1]
    exit(1)

log_flag = 0
shift_flag = 0

for flag in sys.argv[3:]:
    if flag == 'PosNeg':
        color = 8192
    elif flag == 'InvertedPosNeg':
        color = 16384
    elif flag == 'Phase':
        color = 256
    elif flag == 'InvertedPhase':
        color = 4096
    elif flag == 'Jet':
        color = 16
    elif flag == 'Gray':
        color = 1
    elif flag == 'Log':
        log_flag = 1
    elif flag == 'Shift':
        shift_flag = 1
    else:
        print "unknown flag %s" % flag

if log_flag == 1:
    color += 128

if shift_flag == 1:
    img = spimage.sp_image_shift(img)

try:
    spimage.sp_image_write(img,sys.argv[2],color)
except:
    print "Error: Can not write %s\n" % sys.argv[2]
    exit(1)


