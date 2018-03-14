#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob

# md5file = the abspath of original md5file generated in the runfolder prior to transfer to backup

# rf = the abspath of original runfolder prior to transfer to backup

def main(rf, destination):

    filepath = os.path.abspath(rf)
    checkfile = str(datetime.datetime.now()) + ".chk"
    errorfile = str(datetime.datetime.now()) + ".err"

    if not sys.argv2:
        print 'The directory given does not exist'

    bam_list = sorted.glob.glob("{}/bams/*.bam".format(str(rf)))
    vcf_list = sorted.glob.glob("{}/vcfs/*.vcf".format(str(rf)))

    md5_list = []

    for bam in bam_list:
        md5file = bam + ".md5"
        print md5file 
        if not os.path.exists(md5file):
        print "md5file for {} do not exist".format(bam)
        continue

    """if not md5file:
            print 'The md5file do not exist, creating a new md5file'
            createmd5 = "md5sum rf/*.bam /vcfs/*.vcf *.vcf > hash.md5"
            subprocess.call(createmd5, shell=True)
            copymd5 = "cp rf/hash.md5 > destination/md5file"
            subprocess.call(copymd5, shell=True) """

    if checkfile:
        print 'This folder has already been checked today'
    
    else:
        createchk = "touch ./{}".format(checkfile)
        subprocess.call(createchk, shell=True)

    for file in bam_list:

        bamchk = "md5sum -c {} >> {} 2>> {}".format(file, checkfile, errorfile)
        subprocess.call(bamchk, shell=True)
        print

    for file in vcf_list:

        vcfchk = "md5sum -c {} >> {} 2>> {}".format(file, checkfile, errorfile)
        subprocess.call(vcfchk, Shell=True)

        #copy=sh.awk("'{print $1}'hash.md5")

        #original=sh.awk("'{print $1}'filepath/hash.md5")
    
        #if copy == original:
            #checkfile.append("file integrity intact\n")
            #continue
        #else:
            #checkfile.append("file integrity compromised\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])