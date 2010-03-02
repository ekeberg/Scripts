#! /usr/bin/python

import spimage, sys

if len(sys.argv) <= 1:
    print """
Usage:  python_script_shift_image <in.h5> [out.h5]

If no output image is given the origninal image will
be overwritten.
"""
    exit(1)

try:
    img = spimage.sp_image_read(sys.argv[1],0)
except:
    print "Error: Can not read image %s" % sys.argv[1]
    exit(1)

img_s = spimage.sp_image_shift(img)

if len(sys.argv) > 2:
    out = sys.argv[2]
else:
    out = sys.argv[1]

try:
    spimage.sp_image_write(img_s,out,0)
except:
    print "Error: Can not write to %s" % out
