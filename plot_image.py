#! /usr/bin/python

import spimage, pylab, sys

if len(sys.argv) <= 1:
    print """
Usage:  python_script_plot_image <image.h5> [arguments]

Arguments:
abs    plot the absolute value of the image (default)
mask   plot the image mask
phase  plot the phase of the image
log    plot the image in log scale 
shift  shift the image before plotting

Several or none of the above arguments might be combined

"""
    exit(1)

try:
    img = spimage.sp_image_read(sys.argv[1],0)
except:
    print "Error: %s is not a readable .h5 file\n" % sys.argv[1]
    exit(1)

plot_flags = ['abs','mask','phase','real','imag']
shift_flags = ['shift']
log_flags = ['log']

plot_flag = 0
shift_flag = 0
log_flag = 0

for flag in sys.argv[2:]:
    if flag in plot_flags:
        plot_flag = flag
    elif flag in shift_flags:
        shift_flag = flag
    elif flag in log_flags:
        log_flag = flag
    else:
        print "unknown flag %s" % flag

if shift_flag:
    img = spimage.sp_image_shift(img)

def no_log(x):
    return x

if log_flag:
    log_function = pylab.log
else:
    log_function = no_log

if (plot_flag == "mask"):
    pylab.imshow(img.mask,origin='lower',interpolation="nearest")
elif(plot_flag == "phase"):
    pylab.imshow(pylab.angle(img.image),cmap='hsv',origin='lower',interpolation="nearest")
elif(plot_flag == "real"):
    pylab.imshow(log_function(pylab.real(img.image)),origin='lower',interpolation="nearest")
elif(plot_flag == "imag"):
    pylab.imshow(log_function(pylab.imag(img.image)),origin='lower',interpolation="nearest")
else:
    pylab.imshow(log_function(abs(img.image)),origin='lower',interpolation="nearest")

pylab.show()
