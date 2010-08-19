#! /usr/bin/python
import sys, h5py, pylab, spimage

def split_pnccd(filename):
    try:
        f = h5py.File(filename)
    except:
        print "Error reading file %s. It may not be a pnCCD file." % filename
        exit(1)

    data1 = f.values()[1].values()[3].value
    data2 = f.values()[1].values()[4].value

    data2_1 = spimage.sp_image_alloc(data2.shape[1],data2.shape[0]/2,1)
    data2_2 = spimage.sp_image_alloc(data2.shape[1],data2.shape[0]/2,1)
    data2_1.image[:,:] = data2[:(data2.shape[1]/2),:]
    data2_2.image[:,:] = data2[(data2.shape[1]/2):,:]

    spimage.sp_image_write(data2_1,filename[:-3]+"_part1.h5",0)
    spimage.sp_image_write(data2_2,filename[:-3]+"_part2.h5",0)
    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print """
Usage: view_pnccd <filename.h5>

This program is used to view the output from cass.

"""
        exit(0)
    
    split_pnccd(sys.argv[1])
