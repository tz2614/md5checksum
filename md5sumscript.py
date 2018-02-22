#!usr/bin/python

import datetime
import sys
import os
import sh

# md5file = the abspath of original md5file generated in the runfolder prior to transfer to backup

# rf = the abspath of original runfolder prior to transfer to backup

def main(rf, destination, md5file):

    filepath = os.path.abspath(rf)
    checkfile = _datetime.datetime.now()

    if not sys.argv2:
        print 'The directory given does not exist'

    if not md5file:
        print 'The md5file do not exist, creating a new md5file'
        sh.md5sum("rf/*.bam /vcfs/*.vcf *.vcf > hash.md5")
        sh.cp("rf/hash.md5 ")

    if checkfile:
        print 'This folder has already been checked today'
    else:
        sh.touch("./$1_$checkfile")

    for line in "~/rf/hash.md5":

        copy=sh.awk("'{print $1}'hash.md5")

        original=sh.awk("'{print $1}'filepath/hash.md5")
    
        if copy == original:
            checkfile.append("file integrity intact\n")
            continue
        else:
            checkfile.append("file integrity compromised\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

