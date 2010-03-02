#!/usr/bin/env python

"""
This program converts all .h5 files in the current
directory to .png using the HAWK program
image_to_png
"""

import os, re, sys, spimage

l = os.popen('ls').readlines()

expr = re.compile('.h5$')
files = filter(expr.search,l)

if len(sys.argv) == 1:
    for f in files:
        os.system("image_to_png %s %s" % (f[:-1],f[:-3] + "png"))
elif sys.argv[1] == "support":
    for f in files:
        img = spimage.sp_image_read(f[:-1],0)
        spimage.sp_image_mask_to_image(img,img)
        spimage.sp_image_write(img,f[:-3]+"png",16)
        spimage.sp_image_free(img)
