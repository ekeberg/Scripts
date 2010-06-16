#! /usr/bin/python

import spimage, pylab, sys

def crop_image(in_file, out_file, sideX, sideY = 0):
    if sideY = 0:
        sideY = sideX
    print "argv[1] = ", sys.argv[1]
    print "argv[2] = ", sys.argv[2]
    print "argv[3] = ", sys.argv[3]

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

    print "shifted = ", shifted

    lowX = int(img.detector.image_center[0]-(sideX/2.0-0.5))
    highX = int(img.detector.image_center[0]+(sideX/2.0-0.5))
    lowY = int(img.detector.image_center[1]-(sideY/2.0-0.5))
    highY = int(img.detector.image_center[1]+(sideY/2.0-0.5))

    print lowX, " ", highX
    print lowY, " ", highY

    cropped = spimage.rectangle_crop(img,lowX,lowY,highX,highY)

    print "did crop"

    if shifted:
        cropped = spimage.sp_image_shift(cropped)

    print "shifted (or not)"

    print "write ", sys.argv[2]

    print "orientation = ", cropped.detector.orientation
    print sp_3matrix_get(cropped.detector.orientation,0,0)

    try:
        spimage.sp_image_write(cropped,sys.argv[2],16)
    except:
        print "Error: can not write to %s\n" % sys.argv[2]

    print "end"

if __name__ == "__main__":
    try:
        yside = 0
        try:
            yside = sys.argv[4]
        crop_image(str(sys.argv[1]),str(sys.argv[2]),int(sys.argv[3]),yside)
    except:
        print """
Usage:  python_script_crop_image <in.h5> <out.h5> xside [yside]

Crops the image to the specified size symmetrically
around the image center. If only one side is given
xside is used for both sides.
"""


