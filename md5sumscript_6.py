#!usr/bin/python

import datetime
import sys
import os
import subprocess
import pprint as pp
import timeit


""" md5file = the abspath of the md5file generated in the original runfolder that have been copied into the backup runfolder."""

""" rf = the abspath of backup runfolder """

def create_two_lists(rf_path):

    #The following creates a list of bam file and a list of md5 files to check the file integrity of all bam files in the specified directory.

    #assert (rf_path.startswith("/mnt/storage/data/NGS") or runfolders.startswith("/mnt/archive/data/NGS")), "runfolder given incorrect"

    bam_list = []
    md5_list = []
    for root, dirname, filenames in os.walk(rf_path):
        for filename in filenames:
            if filename.endswith(".bam"):
                bam_list.append(os.path.join(root, filename))
            if filename.split(".")[-2] == "bam" and filename.endswith(".md5"):
                md5_list.append(os.path.join(root, filename))
    create_list = [os.path.abspath(bam) for bam in bam_list]
    #print ("create_list:", create_list)
    check_list = [os.path.abspath(md5) for md5 in md5_list]
    #print ("check_list:", check_list)
    
    return list(set(create_list)), list(set(check_list))

def create_md5(create_list, rf_path):

    """For each bam file in the create_list, check if .md5 exist. If not create .md5 file"""

    for bam in create_list:
        #print (bam)
        bam_dir = os.path.dirname(bam)

        #put datetime.datetime.now() for every log entry

        if bam.endswith(".bam"):
            md5file = bam + ".md5"
            #print (md5file)
            md5_dir = os.path.dirname(md5file)

        if os.path.exists(bam):
            print ("{} exist".format(bam))
            with open(os.path.join(bam_dir, "bam_check.txt"), 'a') as bam_check:
                bam_check.writelines("{} exist\n".format(bam))
                continue
        else:
            print ("{} file missing".format(bam))
            with open(os.path.join(bam_dir, "bam_check.txt"), 'a') as bam_check:
                bam_check.writelines("{} file missing".format(bam))
                bam_check.writelines("time of check:{}".format(datetime.datetime.now()))
                continue
        
        if os.path.exists(md5file):
            print ("{} already exist".format(md5file))
            with open(os.path.join(md5_dir, "md5_missing.txt"), 'a') as md5_check:
                md5_check.writelines("{} already exist\n".format(md5file))
                continue

        else:
            print ("{} file missing its associated md5".format(bam))
            createmd5 = "md5sum {} > {}".format(bam, md5file)
            print ("creating a new md5 file: {}".format(md5file))
            subprocess.call(createmd5, shell=True)
            print ("new md5 file {} generated".format(md5file))
            with open (os.path.join(md5_dir, 'md5_missing.txt'), 'a') as new_md5:
                new_md5.writelines('new md5 file {} generated\n'.format(md5file))
                continue
                
    return create_list

def create_logfile(rf_path):

    """create a log file in the specified directory called DATE.chk file"""

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    checkfilepath = os.path.abspath(checkfilepath)
    #print ("checkfilepath created")

    if os.path.exists(checkfilepath):
        print ('{} has already been checked today'.format(checkfilepath))

    else:
        createchk = "touch {}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print ("check log {} generated".format(checkfilepath))

    return checkfilepath

def check_md5(checkfilepath, check_list):

    """Check the file integrity of bam files in the runfolder using md5sum -c for all the bam associated .md5 files in the check_list"""
    
    for md5 in check_list:
        #print (md5)
        
        if md5.endswith(".md5"): 
            with open (checkfilepath, 'a') as md5_check:
                md5_check.writelines("{} file is being checked\n".format(md5))
            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5, checkfilepath, checkfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)
            print ("{} checked".format(md5))
    
    return check_list

def check_org_bkup(org_rf_path, bkup_rf_path, org_check_list, bkup_check_list):

    """check that .md5 in the current runfolder match that in the backup runfolder, 
    if the md5sum hash value do not match, or that the path to the bam file do not match
    raise an error on terminal, and record the error in the error log"""

    check_dict = {}
    check_dict["storage"] = {}
    check_dict["archive"] = {}

    print ("checking md5s between original and backup runfolders")

    #check the .md5 file contain the correct format, and have the correct hash and bam file name associated with it in both backup and original runfolder.

    for md5 in org_check_list:
        
        md5_dir = os.path.dirname(md5)
        #print (md5_dir)
        bam_filename = ".".join(md5.split("/")[-1].split(".")[:-1])
        #print (bam_filename)
        md5_filename = md5.split("/")[-1]
        #print (md5_filename)

        with open (md5) as md5_file:
            for line in md5_file:
                fields = line.strip().split("  ")
                if len(fields[0]) != 32:
                    #comments
                    print ("{} hash do not have 32 characters".format(md5))
                    with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} hash do not have 32 characters".format(md5))
                
                bam = fields[1].split("/")[-1]
                if bam != bam_filename:
                    #comments
                    print ("{} do not match {} in {}".format(bam_filename, bam, md5))
                    with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} do not match {} in {}\n".format(bam_filename, bam, md5))
                    
                else:
                    if md5_filename in check_dict["storage"]:
                        #comments
                        print ("{} already in {}".format(md5_filename, md5_dir))
                        with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                            org_bkup_check.writelines("{} already in {}, duplicate found\n".format(md5_filename, md5_dir))
                    else:
                        check_dict["storage"][md5_filename] = fields[0]
    
    for md5 in bkup_check_list:

        md5_dir = os.path.dirname(md5)
        #print (md5_dir)
        bam_filename = ".".join(md5.split("/")[-1].split(".")[:-1])
        #print (bam_filename)
        md5_filename = md5.split("/")[-1]
        #print (md5_filename)

        with open (md5) as md5_file:
            for line in md5_file:
                fields = line.strip().split("  ")

                if len(fields[0]) != 32:
                    print ("{} hash do not have 32 characters".format(md5))
                    with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} hash do not have 32 characters".format(md5_filename))

                bam = fields[1].split("/")[-1]
                if bam != bam_filename:
                    print ("{} do not match {} in {}".format(bam_filename, bam, md5))
                    with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                        org_bkup_check.writelines("{} do not match {} in {}\n".format(bam_filename, bam, md5))

                else:        
                    if md5_filename in check_dict["archive"]:
                        print ("{} already in {}".format(md5, md5_dir))
                        with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
                            org_bkup_check.writelines("{} already in {}, duplicate found\n".format(md5_filename, md5_dir))
                    check_dict["archive"][md5_filename] = fields[0]

    #excess_md5s = set(org_md5_list) ^ set(bkup_md5_list)
        
    #comments to explain what each dictionary stores 
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

    for md5_filename in check_dict["archive"]:

        #comment on what each statememnt checks

        print ("{} being compared".format(md5_filename))
        with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("{} being compared\n".format(md5_filename))

        if md5_filename in check_dict["storage"] and check_dict["archive"][md5_filename] == check_dict["storage"][md5_filename]:
            print ("OK {}".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "md5_match.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("OK {} \n".format(md5_filename))
            md5_matches["backup"][md5_filename] = check_dict["archive"][md5_filename]
        
        if md5_filename in check_dict["storage"] and check_dict["archive"][md5_filename] != check_dict["storage"][md5_filename]:
            print ("ERROR, mismatch found, {} name matches the file in original folder, but the hash do not match".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} name matches the original folder, but the hash do not match\n".format(md5_filename))
            md5_mismatches["backup"][md5_filename] = check_dict["archive"][md5_filename]

        if md5_filename not in check_dict["storage"] and check_dict["archive"][md5_filename] not in check_dict["storage"].values():
            print ("ERROR, mismatch found, {} not in original folder".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in original folder\n".format(md5_filename))
            md5_in_bkup_not_org["no hash match"][md5_filename] = check_dict["archive"][md5_filename]

        if md5_filename not in check_dict["storage"] and check_dict["archive"][md5_filename] in check_dict["storage"].values():
            print ("ERROR, mismatch found, {} not in original folder, but matches hash of another .md5 in the original folder".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in original folder, but matches hash of another .md5 in the original folder\n".format(md5_filename))
            md5_in_bkup_not_org["hash match"][md5_filename] = check_dict["archive"][md5_filename]

    for md5_filename in check_dict["storage"]:

        print ("{} being compared".format(md5_filename))
        with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("{} being checked\n".format(md5_filename))

        if md5_filename in check_dict["archive"] and check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
            print ("OK {}".format(md5_filename))
            with open (os.path.join(org_rf_path, "md5_match.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("OK {} \n".format(md5_filename))
            md5_matches["original"][md5_filename] = check_dict["storage"][md5_filename]

        if md5_filename in check_dict["archive"] and check_dict["storage"][md5_filename] != check_dict["archive"][md5_filename]:
            print ("ERROR, mismatch found, {} name matches the file in backup folder, but the hash do not match".format(md5_filename))
            with open (os.path.join(org_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} name matches the backup folder, but the hash do not match\n".format(md5_filename))
            md5_mismatches["original"][md5_filename] = check_dict["storage"][md5_filename]

        if md5 not in check_dict["archive"] and check_dict["storage"][md5_filename] not in check_dict["archive"].values():
            print ("ERROR, mismatch found, {} not in backup folder".format(md5_filename))
            with open (os.path.join(org_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in backup folder\n".format(md5_filename))
            md5_in_org_not_bkup["no hash match"][md5_filename] = check_dict["storage"][md5_filename]

        if md5_filename not in check_dict["archive"] and check_dict["storage"][md5_filename] in check_dict["archive"].values():
            print ("ERROR, mismatch found, {} not in backup folder, but matches hash of another .md5 in the backup folder".format(md5_filename))
            with open (os.path.join(org_rf_path, "md5_mismatch.txt"), "a") as org_bkup_check:
                org_bkup_check.writelines("ERROR, mismatch found, {} not in backup folder, but matches hash of another .md5 in the backup folder\n".format(md5_filename))
            md5_in_org_not_bkup["hash match"][md5_filename] = check_dict["storage"][md5_filename]


    if md5_mismatches["original"] or md5_mismatches["backup"]:
        pp.pprint(md5_mismatches)
    else:
        print "no md5 mismatch found"

    if md5_in_bkup_not_org["hash match"] or md5_in_bkup_not_org["no hash match"]:
        pp.pprint(md5_in_bkup_not_org)
    else:
        print "all backup .md5 present in original runfolder"

    if md5_in_org_not_bkup["hash match"] or md5_in_org_not_bkup["no hash match"]:
        pp.pprint(md5_in_org_not_bkup)
    else:
        print "all original .md5 present in backup runfolder"


def main(org_rf_path, bkup_rf_path, wkdir):

    #start timer
    start = timeit.default_timer()

    #generate a create_list and check_list for both original and backup runfolder
    org_create_list, org_check_list = create_two_lists(org_rf_path)
    bkup_create_list, bkup_check_list = create_two_lists(bkup_rf_path)

    #check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it.
    create_md5(org_create_list, org_rf_path)
    create_md5(bkup_create_list, bkup_rf_path)

    #check bam file integrity within runfolder
    checkfilepath1 = create_logfile(org_rf_path)
    checkfilepath2 = create_logfile(bkup_rf_path)
    check_md5(checkfilepath1, org_check_list)
    check_md5(checkfilepath2, bkup_check_list)

    #check md5sum values and bam filenames within .md5 match between original and backup runfolder
    check_org_bkup(org_rf_path, bkup_rf_path, org_check_list, bkup_check_list)

    #end timer
    end = timeit.default_timer()

    timetaken = end - start
    print ("estimate of program run time:{}".format(timetaken))
    with open(os.path.join(wkdir, 'time.txt'), 'a') as time_text:
            time_text.writelines("time taken to check bam file integrity in {}\n and {}: {} \n".format(org_rf_path, bkup_rf_path, timetaken))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

#navigate to where the script is located from command line, and enter "python", then the name of the script "md5sumcript_5.py"

#followed by the runfolder you wish to check - sys.argv[1]
