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

"""
    org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
    org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
    org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
    org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
    org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
    org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
    org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
    org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
    org_rf_path_9, bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_sample_bam_9 = scenario_9_fixture()

    org_bam_list_1, org_md5_list_1 = md5sumscript.create_two_lists(org_rf_path_1)
    bkup_bam_list_1, bkup_md5_list_1 = md5sumscript.create_two_lists(bkup_rf_path_1)

    org_bam_list_2, org_md5_list_2 = md5sumscript.create_two_lists(org_rf_path_2)
    bkup_bam_list_2, bkup_md5_list_2 = md5sumscript.create_two_lists(bkup_rf_path_2)

    org_bam_list_3, org_md5_list_3 = md5sumscript.create_two_lists(org_rf_path_3)
    bkup_bam_list_3, bkup_md5_list_3 = md5sumscript.create_two_lists(bkup_rf_path_3)

    org_bam_list_4, org_md5_list_4 = md5sumscript.create_two_lists(org_rf_path_4)
    bkup_bam_list_4, bkup_md5_list_4 = md5sumscript.create_two_lists(bkup_rf_path_4)

    org_bam_list_5, org_md5_list_5 = md5sumscript.create_two_lists(org_rf_path_5)
    bkup_bam_list_5, bkup_md5_list_5 = md5sumscript.create_two_lists(bkup_rf_path_5)

    org_bam_list_6, org_md5_list_6 = md5sumscript.create_two_lists(org_rf_path_6)
    bkup_bam_list_6, bkup_md5_list_6 = md5sumscript.create_two_lists(bkup_rf_path_6)

    org_bam_list_7, org_md5_list_7 = md5sumscript.create_two_lists(org_rf_path_7)
    bkup_bam_list_7, bkup_md5_list_7 = md5sumscript.create_two_lists(bkup_rf_path_7)

    org_bam_list_8, org_md5_list_8 = md5sumscript.create_two_lists(org_rf_path_8)
    bkup_bam_list_8, bkup_md5_list_8 = md5sumscript.create_two_lists(bkup_rf_path_8)

    org_bam_list_9, org_md5_list_9 = md5sumscript.create_two_lists(org_rf_path_9)
    bkup_bam_list_9, bkup_md5_list_9 = md5sumscript.create_two_lists(bkup_rf_path_9)

    new_md5_list1 = md5sumscript.create_md5(bam_list1, org_rf_path_1)
    new_md5_list7 = md5sumscript.create_md5(bam_list7, org_rf_path_7)
    new_md5_list8 = md5sumscript.create_md5(bam_list8, org_rf_path_8)
    new_md5_list9 = md5sumscript.create_md5(bam_list9, org_rf_path_9)

    md5_list = [new_org_sample_md5_1, new_org_sample_md5_2, new_org_sample_md5_3, new_org_sample_md5_4, new_org_sample_md5_5, new_org_sample_md5_6, new_org_sample_md5_7, new_bkup_sample_md5_1, new_bkup_sample_md5_2, new_bkup_sample_md5_3, new_bkup_sample_md5_4, new_bkup_sample_md5_5, new_bkup_sample_md5_6, new_bkup_sample_md5_8]
    
    check_dict = md5sumscript.create_check_dict(orgfilepath, bkupfilepath, org_md5_list, bkup_md5_list)
"""
    