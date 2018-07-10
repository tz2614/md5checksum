#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re
#import fnmatch


""" md5file = the abspath of the md5file generated in the original runfolder that have been copied into the backup runfolder."""

""" rf = the abspath of backup runfolder """

def check_md5(checkfilepath, errorfilepath, check_list):

    """for each file in the specified folder, check if .md5 exist."""

    for md5 in check_list:
        md5file = md5 + ".md5"
        #print md5file 
        
        if md5.endswith(".md5"): 
            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5, checkfilepath, errorfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print "{} checked".format(md5)
        else:
            if not os.path.exists(md5file):
                print "md5file for {} do not exist".format(md5)
            continue
    return

def create_md5_list(rf_path):

    """create a list of md5 files to check against within the specified directory"""

    #The following creates a list of files to check the file integrity of all files in the specified directory recursively.
    md5_list = []
    for root, dirname, filenames in os.walk(rf_path):
        for filename in filenames:
            md5_list.append(os.path.join(root, filename))
    #print (md5_list)
    create_exclude_list = ["md5", "chk", "err"]
    check_exclude_list = ["chk", "err"]
    create_list = [x for x in md5_list if x.split(".")[-1] not in create_exclude_list]
    check_list = [x for x in md5_list if x.split(".")[-1] not in check_exclude_list]
    return create_list, check_list

    #md5_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))

def create_logfiles(rf_path):

    """create two log files in the specified directory, one is the .chk file, the other is the .err log"""

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