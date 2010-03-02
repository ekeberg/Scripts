#! /usr/bin/python

import spimage, pylab, sys

if len(sys.argv) <= 3:
    print """
Usage:  python_script_crop_image <in.h5> <out.h5> xside [yside]

Crops the image to the specified size symmetrically
around the image center. If only one side is given
xside is used for both sides.
"""
    exit(1)

try:
    img = spimage.sp_image_read(sys.argv[1],0)
except:
    print "Error: %s is not a readable .h5 file\n" % sys.argv[1]
    exit(1)

try:
    sideX = int(sys.argv[3])
except:
    print "Error: %s is not an int\n" % sys.argv[3]
    exit(1)
try:
    sideY = int(sys.argv[4])
except:
    sideY = sideX

shifted = 0
if img.shifted:
    shifted = 1
    img = spimage.sp_image_shift(img)

lowX = int(img.detector.image_center[0]-(sideX/2.0-0.5))
highX = int(img.detector.image_center[0]+(sideX/2.0-0.5))
lowY = int(img.detector.image_center[1]-(sideY/2.0-0.5))
highY = int(img.detector.image_center[1]+(sideY/2.0-0.5))

cropped = spimage.rectangle_crop(img,lowX,lowY,highX,highY)

if shifted:
    cropped = spimage.sp_image_shift(cropped)

try:
    spimage.sp_image_write(cropped,sys.argv[2],0)
except:
    print "Error: can not write to %s\n" % sys.argv[1]
