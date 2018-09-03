#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re
import pprint as pp
import timeit
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
    #print ("create_list:", create_list)
    check_list = md5_list
    #print ("check_list:", check_list)
    
    return create_list, check_list

    #md5_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))

def create_md5(create_list, rf_path):

    """For each bam file in the create_list, check if .md5 exist. If not create .md5 file"""

    for bam in create_list:
        #print (bam)
        if bam.endswith(".bam"):
            md5file = bam + ".md5"
            #print (md5file)
        
            if not os.path.exists(md5file):
                createmd5 = "md5sum {} > {}".format(bam, md5file)
                print (createmd5)
                subprocess.call(createmd5, shell=True)
                print ("new md5 file {} generated".format(md5file))
                with open (os.path.join(rf_path, 'md5_check.txt'), 'a') as new_md5:
                    new_md5.writelines('new md5 file {} generated\n'.format(md5file))
            else:
                print ("{} already exist".format(md5file))
                with open(os.path.join(rf_path, "md5_check.txt"), 'w') as md5_check:
                    md5_check.writelines("{} already exist\n".format(md5file))
                    continue

    return create_list

def create_logfiles(rf_path):

    """create two log files in the specified directory, one is the .chk file, the other is the .err log"""

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    #print ("checkfilepath created")

    errorfile = str(datetime.datetime.now()).split(" ")[0] + ".err"
    errorfilepath = os.path.join(rf_path, errorfile)
    #print ("errorfilepath created")
    
    if os.path.exists(checkfilepath):
        print ('{} has already been checked today'.format(rf_path))

    else:
        createchk = "touch /{}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print ("check log {} generated".format(checkfilepath))
        createerr = "touch /{}".format(errorfilepath)
        subprocess.call(createerr, shell=True)
        print ("error log {} generated".format(errorfilepath))

    return checkfilepath, errorfilepath         

def check_md5(wdir, checkfilepath, errorfilepath, check_list):

    """Check the file integrity of bam files in the runfolder using md5sum -c for all the bam associated .md5 files in the check_list"""
    
    for md5 in check_list:
        #print (md5)
        
        if md5.endswith(".md5"): 
            with open (checkfilepath, 'a') as md5_check:
                md5_check.writelines("{} file is being checked\n".format(md5))
            with open (errorfilepath, 'a') as md5_err:
                md5_err.writelines("{} file is being checked\n".format(md5))
            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5, checkfilepath, errorfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print ("{} checked".format(md5))

        elif not os.path.exists(md5):
            print ("md5file for {} do not exist".format(md5))
            with open (os.path.join(wdir, "md5_missing.txt"), "a") as md5_missing:
                md5_missing.writelines("{}\n".format(md5))
    
    return check_list

def check_org_bkup(wdir, org_check_list, bkup_check_list):

    """check that .md5 in the current runfolder match that in the backup runfolder, 
    if the md5sum hash value do not match, or that the path to the bam file do not match
    raise an error on terminal, and record the error in the error log"""

    org_dict = {}
    bkup_dict = {}
    org_md5_list = []
    bkup_md5_list = []

    print ("checking md5s between original and backup runfolders")

    #check the .md5 file contain the correct format, and have the correct hash and bam file name associated with it.

    for md5 in org_check_list:
        md5_dir = os.path.dirname(md5)
        print ("{} being checked".format(md5))
        with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("{} being checked\n".format(md5))
        #print (md5_dir)
        bam_filename = ".".join(md5.split("/")[-1].split(".")[:-1])
        #print (bam_filename)
        md5_filename = md5.split("/")[-1]
        #org_md5_list.append(md5_filename)
        #print (md5_filename)
        with open (md5) as md5_file:
            for line in md5_file:
                fields = line.strip().split("  ")
                if len(fields[0]) != 32:
                    print ("{} hash do not have 32 characters".format(md5))
                    with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} hash do not have 32 characters".format(md5))
                
                bam = fields[1].split("/")[-1]
                if bam != bam_filename:
                    print ("{} do not match {} in {}".format(bam_filename, bam, md5))
                    with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} do not match {} in {}\n".format(bam_filename, bam, md5))
                    
                else:
                    if md5_filename in org_dict:
                        print ("{} already in {}".format(md5_filename, md5_dir))
                        with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                            org_bkup_check.writelines("{} already in {}, duplicate found\n".format(md5_filename, md5_dir))
                    org_dict[md5] = fields[0]
    
    for md5 in bkup_check_list:
        md5_dir = os.path.dirname(md5)
        print ("{} being checked".format(md5))
        with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("{} being checked\n".format(md5))
        #print (md5_dir)
        bam_filename = ".".join(md5.split("/")[-1].split(".")[:-1])
        #print (bam_filename)
        md5_filename = md5.split("/")[-1]
        #bkup_md5_list.append(md5_filename)
        #print (md5_filename)
        with open (md5) as md5_file:

            for line in md5_file:
                fields = line.strip().split("  ")

                if len(fields[0]) != 32:
                    print ("{} hash do not have 32 characters".format(md5_filename))
                    with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} hash do not have 32 characters".format(md5_filename))

                bam = fields[1].split("/")[-1]
                if bam != bam_filename:
                    print ("{} do not match {} in {}".format(bam_filename, bam, md5))
                    with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} do not match {} in {}\n".format(bam_filename, bam, md5))

                else:        
                    if md5_filename in bkup_dict:
                        print ("{} already in {}".format(md5_filename, md5_dir))
                        with open (os.path.join(wdir, "org_bkup_check.txt"), "a") as org_bkup_check:
                            org_bkup_check.writelines("{} already in {}, duplicate found\n".format(md5_filename, md5_dir))
                    bkup_dict[md5] = fields[0]

    #excess_md5s = set(org_md5_list) ^ set(bkup_md5_list)
        
    md5_matches = {}
    md5_matches["original"] = {}
    md5_matches["backup"] = {}
    md5_mismatches = {}
    md5_mismatches["original"] = {}
    md5_mismatches["backup"] = {}
    md5_in_org_not_bkup = {}
    md5_in_org_not_bkup["hash match"] = {}
    md5_in_org_not_bkup["no hash match"] = {}
    md5_in_bkup_not_org = {}
    md5_in_bkup_not_org["hash match"] = {}
    md5_in_bkup_not_org["no hash match"] = {}

    for md5 in bkup_dict:
        if md5 in org_dict and bkup_dict[md5] == org_dict[md5]:
            print ("OK {}".format(md5))
            with open (os.path.join(wdir, "md5_match.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("OK {} \n".format(md5))
            md5_matches["backup"][md5] = bkup_dict[md5]
        
        if md5 in org_dict and bkup_dict[md5] != org_dict[md5]:
            print ("ERROR, mismatch found, {} name matches the file in original folder, but the hash do not match".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} name matches the original folder, but the hash do not match\n".format(md5))
            md5_mismatches["backup"][md5] = bkup_dict[md5]

        if md5 not in org_dict and bkup_dict[md5] not in org_dict.values():
            print ("ERROR, mismatch found, {} not in original folder".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in original folder\n".format(md5))
            md5_in_bkup_not_org["no hash match"][md5] = bkup_dict[md5]

        if md5 not in org_dict and bkup_dict[md5] in org_dict.values():
            print ("ERROR, mismatch found, {} file not present in original folder, but matches hash of another .md5 in the original folder".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} file not present in original folder, but matches hash of another .md5 in the original folder\n".format(md5))
            md5_in_bkup_not_org["hash match"][md5] = bkup_dict[md5]

    for md5 in org_dict:
        if md5 in bkup_dict and bkup_dict[md5] == org_dict[md5]:
            print ("OK {}".format(md5))
            with open (os.path.join(wdir, "md5_match.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("OK {} \n".format(md5))
            md5_matches["original"][md5] = org_dict[md5]

        if md5 in bkup_dict and org_dict[md5] != bkup_dict[md5]:
            print ("ERROR, mismatch found, {} name matches the file in backup folder, but the hash do not match".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} name matches the backup folder, but the hash do not match\n".format(md5))
            md5_mismatches["original"][md5] = org_dict[md5]

        if md5 not in bkup_dict and org_dict[md5] not in bkup_dict.values():
            print ("ERROR, mismatch found, {} not in backup folder".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in backup folder\n".format(md5))
            md5_in_org_not_bkup["no hash match"][md5] = org_dict[md5]

        if md5 not in bkup_dict and org_dict[md5] in bkup_dict.values():
            print ("ERROR, mismatch found, {} file not present in backup folder, but matches hash of another .md5 in the backup folder".format(md5))
            with open (os.path.join(wdir, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} file not present in backup folder, but matches hash of another .md5 in the backup folder\n".format(md5))
            md5_in_org_not_bkup["hash match"][md5] = org_dict[md5]


            pp.pprint(md5_mismatches)
            pp.pprint(md5_matches)
            pp.pprint(md5_in_bkup_not_org)
            pp.pprint(md5_in_org_not_bkup)


def main(original_rf, backup_rf, wdir):

    #start timer
    start = timeit.default_timer()

    #convert runfolder in to runfolder path
    org_rf_path = os.path.abspath(original_rf)
    bkup_rf_path = os.path.abspath(backup_rf)

    #generate a create_list and check_list for original and backup runfolder
    org_create_list, org_check_list = create_two_lists(org_rf_path)
    bkup_create_list, bkup_check_list = create_two_lists(bkup_rf_path)

    #check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it.
    create_md5(org_create_list, org_rf_path)
    create_md5(bkup_create_list, bkup_rf_path)

    #check bam file integrity within original runfolder
    org_checkfilepath, org_errorfilepath = create_logfiles(org_rf_path)
    check_md5(wdir, org_checkfilepath, org_errorfilepath, org_check_list)

    #check bam file integrity within backup runfolder
    bkup_checkfilepath, bkup_errorfilepath = create_logfiles(bkup_rf_path)
    check_md5(wdir, bkup_checkfilepath, bkup_errorfilepath, bkup_check_list)

    #check md5sum values and bam filenames within .md5 match between original and backup runfolder
    check_org_bkup(wdir, org_check_list, bkup_check_list)

    #end timer
    end = timeit.default_timer()

    print "estimate of program run time:", end - start

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])