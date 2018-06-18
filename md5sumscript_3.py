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

    rf_path = os.path.abspath(rf)
    create_list, check_list = create_md5_list(rf_path)
    create_md5(rf, create_list)
    checkfilepath, errorfilepath = create_logfiles(rf_path)
    check_md5(checkfilepath, errorfilepath, check_list)
    
def check_md5(checkfilepath, errorfilepath, check_list)

    for md5 in check_list:
        md5file = md5 + ".md5"
        #print md5file 
        
        if not os.path.exists(md5file):
            print "md5file for {} do not exist".format(md5)
            continue
        else:

            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5file, checkfilepath, errorfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print "md5 files checked, see .err and .chk log files for details"
    return

def create_md5_list(rf_path):

    bam_list = sorted(glob.glob("{}/bams/*.bam".format(str(rf_path))))
    vcf_list = sorted(glob.glob("{}/vcfs/*.vcf".format(str(rf_path))))
    otherfile_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))
    md5_list = bam_list + vcf_list + otherfile_list
    create_exclude_list = ["md5", "chk", "err"]
    check_exclude_list = ["chk", "err"]
    create_list = [x for x in md5_list if x.split(".")[-1] not in filetoexclude]
    check_list = [x for x in md5_list if x.split(".")[-1] not in filetoexclude]
    return create_list, check_list

def create_logfiles(rf_path):

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    print "checkfilepath created"

    errorfile = str(datetime.datetime.now()).split(" ")[0] + ".err"
    errorfilepath = os.path.join(rf_path, errorfile)
    print "errorfilepath created"

    if os.path.exists(checkfilepath):
        print 'This folder has already been checked today'
        exit()

    else:
        createchk = "touch /{}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print "check log {} generated".format(createchk)
        createerr = "touch /{}".format(errorfilepath)
        subprocess.call(createerr, shell=True)
        print "error log {}".format(createrr)

    return checkfilepath, errorfilepath

def create_md5(rf, create_list):
    
    for md5 in create_list:
        #print md5
        if any ([md5.endswith(x) for x in filetoexclude]):
            continue

        else:
            md5file = md5 + ".md5"
            #print md5file
        
        if not os.path.exists(md5file):
            createmd5 = "md5sum {} > {}".format(md5, md5file)
            print createmd5
            subprocess.call(createmd5, shell=True)
            print "new md5 file generated"

if __name__ == "__main__":
    main(sys.argv[1])