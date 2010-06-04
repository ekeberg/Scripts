#!/usr/bin/env python

"""
This program converts all .h5 files in the current
directory to .png using the HAWK program
image_to_png
"""

import os, re, sys, spimage

if len(sys.argv) <= 1:
    print """
This program converts all h5 files in the curren directory to png.
Usage:  python_script_to_png [colorscale]

Colorscales:
Jet
Gray
PosNeg
InvertedPosNeg
Phase
InvertedPhase
Log (can be combined with the others)
Shift (can be combined with the others)
Support

"""
    exit(1)


l = os.popen('ls').readlines()

expr = re.compile('.h5$')
files = filter(expr.search,l)

log_flag = 0
shift_flag = 0
support_flag = 0
color = 16

for flag in sys.argv[1:]:
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
    elif flag == 'Support':
        support_flag = 1
    else:
        print "unknown flag %s" % flag

if log_flag == 1:
    color += 128

for f in files:
    img = spimage.sp_image_read(f[:-1],0)

shift_function = spimage.sp_image_shift    
if shift_flag:
    def shift_function(img):
        return img

if support_flag:
    for f in files:
        img = spimage.sp_image_read(f[:-1],0)
        spimage.sp_image_mask_to_image(img,img)
        spimage.sp_image_write(shift_function(img),f[:-3]+"png",color)
        spimage.sp_image_free(img)
else:
    for f in files:
        img = spimage.sp_image_read(f[:-1],0)
        spimage.sp_image_write(shift_function(img),f[:-3]+"png",color)
        spimage.sp_image_free(img)
