#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re

# md5file = the abspath of the md5file generated in the original runfolder that have been copied into the backup runfolder.

# rf = the abspath of backup runfolder 

def main(rf):

    #rf_name_1stpart = rf.split("_")[0]
    #rf_name_lastpart = rf.split("_")[-1]
    #assert re.match(r'[0-9]', rf_name_1stpart), "first part of runfolder name did not match"
    #assert re.match(r'[A-Z][0-9]', rf_name_lastpart), "last part of runfolder name did not match"

    rf_path = os.path.abspath(rf)

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)

    errorfile = str(datetime.datetime.now()).split(" ")[0] + ".err"
    errorfilepath = os.path.join(rf_path, errorfile)

    bam_list = sorted(glob.glob("{}/bams/*.bam".format(str(rf_path))))
    vcf_list = sorted(glob.glob("{}/vcfs/*.vcf".format(str(rf_path))))
    otherfile_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))
    md5_list = bam_list + vcf_list + otherfile_list
    filetoexclude = ["md5", "chk", "err"]

    md5_list = [x for x in md5_list if x.split(".")[-1] not in filetoexclude]


    if os.path.exists(checkfilepath):
        print 'This folder has already been checked today'
        exit()

    else:
        createchk = "touch /{}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print "check log {} generated".format(checkfilepath)
        createerr = "touch /{}".format(errorfilepath)
        subprocess.call(createerr, shell=True)
        print "error log {} generated".format(errorfilepath)

    return checkfilepath, errorfilepath

def create_md5(create_list):

    """ This function is used to create .md5 file for each of the files 
    within the testbamfiles/ directory"""
    
    for x in create_list:
        #print md5
        if x.endswith("md5"):
            continue

        else:
            md5file = x + ".md5"
            #print md5file
        
        if not os.path.exists(md5file):
            createmd5 = "md5sum {} > {}".format(x, md5file)
            print createmd5
            subprocess.call(createmd5, shell=True)
            print "new md5 file generated, {}".format(md5file)

def main(rf):

    rf_path = os.path.abspath(rf)
    create_list, check_list = create_md5_list(rf_path)
    create_md5(create_list)
    checkfilepath, errorfilepath = create_logfiles(rf_path)
    check_md5(checkfilepath, errorfilepath, check_list)

if __name__ == "__main__":
    main(sys.argv[1])
