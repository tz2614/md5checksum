#!usr/bin/python

import datetime
import sys
import os
import subprocess
import pprint as pp
import timeit


def check_filename_duplicate(checkfilepath, md5_filename, md5_dir, check_dict):

    #check if the same md5 filename has been seen before, if so display the name of the file on terminal, and record the duplicate in error log.

    assert os.path.exists(checkfilepath), "checkfile path DO NOT exist"

    rf_path = os.path.abspath(checkfilepath)
    assert os.path.isabs(checkfilepath), "checkfile path NOT absolute"

    if md5_filename in check_dict:

        print ("{} already in {}, duplicate found".format(md5_filename, md5_dir))
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("{} already in {}, duplicate found\n".format(md5_filename, md5_dir))
            return True

    else:
        #print ("{} not in {}, add to dictionary".format(md5_filename, md5_dir))
        #with open (checkfilepath, "a") as md5_check:
            #md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            #md5_check.writelines("{} not in {}, add to dictionary".format(md5_filename, md5_dir))
        return False

def check_md5filenames_in_bkup(rf_path, md5_filename, check_dict):

    """check if md5 file name is present in backup runfolder"""

    assert os.path.exists(rf_path), "runfolder path DO NOT exist"
    
    rf_path = os.path.abspath(rf_path)
    assert os.path.isabs(rf_path), "runfolder path NOT absolute"

    if md5_filename in check_dict["archive"]:
        #print ("{} present in {}".format(md5_filename, "archive"))
        with open (os.path.join(rf_path, "md5_match.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            filename_check.writelines("{} present in {} \n".format(md5_filename, "archive"))
            return True
    else:
        print ("ERROR, {} not in {}".format(md5_filename, "archive"))
        with open (os.path.join(rf_path, "md5_mismatch.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            filename_check.writelines("ERROR, {} not in {} \n".format(md5_filename, "archive"))
            return False

def check_md5filename(rf_path, md5_filename, check_dict):

    """check if md5 file name is present in md5 check dictionary"""

    if md5_filename in check_dict:
        print ("{} present".format(md5_filename))
        with open (os.path.join(rf_path, "md5_match.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            filename_check.writelines("{} present \n".format(md5_filename))
            return True
    else:
        print ("ERROR, {} not present".format(md5_filename))
        with open (os.path.join(rf_path, "md5_mismatch.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            filename_check.writelines("ERROR, {} not in \n".format(md5_filename))
            return False

def check_md5(checkfilepath, md5_path):
    
    """check the file integrity of bam files in the runfolder using md5sum -c for all the bam associated .md5 files in the check_list"""
    
    if md5.endswith(".md5"): 
        with open (checkfilepath, 'a') as md5_check:
            print ("{} file is being checked".format(md5))
            md5_check.writelines("{} file is being checked\n".format(md5))
            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5, checkfilepath, checkfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print ("{} checked".format(md5))

    return checkfilepath

def create_md5_missing_logfile(rf_path):

    log_file = os.path.join(rf_path, "md5_missing.txt")

    log_file = os.path.abspath(log_file)
    assert os.path.isabs(log_file), "md5_missing log file path NOT absolute"
    assert os.path.exists(log_file), "log file {} missing".format(log_file)

    return log_file

    if org_new_md5_list != []:
        org_check_dict2 = check_md5(org_file_path, new_md5_list_in_org)
    org_check_dict.update(org_check_dict2)

    if bkup_new_md5_list != []:
        bkup_check_dict2 = check_md5(bkup_file_path, new_md5_list_in_bkup)
    bkup_check_dict.update(bkup_check_dict2)
    