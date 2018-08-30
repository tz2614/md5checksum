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

def create_two_lists(rf_path):

    #The following creates a list of bam file and a list of md5 files to check the file integrity of all bam files in the specified directory.

    bam_list = []
    md5_list = []
    for root, dirname, filenames in os.walk(rf_path):
        for filename in filenames:
            if filename.endswith(".bam"):
                bam_list.append(os.path.join(root, filename))
            if filename.split(".")[-2] == "bam" and filename.endswith(".md5"):
                md5_list.append(os.path.join(root, filename))
    create_list = bam_list
    print (create_list)
    check_list = md5_list
    print (check_list)
    
    return create_list, check_list

    #md5_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))

def check_md5(checkfilepath, errorfilepath, check_list):

    for md5 in check_list:
        if md5.endswith(".md5"): 
            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5, checkfilepath, errorfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print ("{} checked".format(md5))

        elif not os.path.exists(md5):
            print ("md5file for {} do not exist".format(md5))
            with open (errfilepath, 'a') as md5_check:
                md5_check.writelines("md5file for {} do not exist".format(md5))   
                continue
    
    return md5_check

def create_logfiles(rf_path):

    """create two log files in the specified directory, one is the .chk file, the other is the .err log"""

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    print ("checkfilepath created")

    errorfile = str(datetime.datetime.now()).split(" ")[0] + ".err"
    errorfilepath = os.path.join(rf_path, errorfile)
    print ("errorfilepath created")

    if os.path.exists(checkfilepath):
        print ('This folder has already been checked today')
        exit()

    else:
        createchk = "touch /{}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print ("check log {} generated".format(checkfilepath))
        createerr = "touch /{}".format(errorfilepath)
        subprocess.call(createerr, shell=True)
        print ("error log {} generated".format(errorfilepath))

    return checkfilepath, errorfilepath

def create_md5(create_list):

    """For each bam file in the specified folder, check if .md5 exist. If not, this function is used to create .md5 file"""

    for bam in create_list:
        print (bam)
        if bam.endswith(".bam"):
            md5file = bam + ".md5"
            print (md5file)
        
        if not os.path.exists(md5file):
            createmd5 = "md5sum {} > {}".format(bam, md5file)
            print (createmd5)
            subprocess.call(createmd5, shell=True)
            print ("new md5 file {} generated".format(md5file))
            with open (os.path.join(rf_path, 'new_md5.txt'), 'a') as new_md5:
                new_md5.writelines('new md5 file {} generated'.format(md5file))                

#def check_org_bkup(org_check_list, bkup_check_list):

def main(original_rf, backup_rf):

    org_rf_path = os.path.abspath(original_rf)
    bkup_rf_path = os.path.abspath(backup_rf)
    org_create_list, org_check_list = create_two_lists(org_rf_path)
    bkup_create_list, bkup_check_list = create_two_lists(bkup_rf_path)
    exit()
    create_md5(org_create_list)
    create_md5(bkup_create_list)
    org_checkfilepath, org_errorfilepath = create_logfiles(org_rf_path)
    check_md5(org_checkfilepath, org_errorfilepath, org_check_list)
    bkup_checkfilepath, bkup_errorfilepath = create_logfiles(bkup_rf_path)
    check_md5(bkup_checkfilepath, bkup_errorfilepath, bkup_check_list)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])