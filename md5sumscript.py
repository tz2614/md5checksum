#!usr/bin/python

import datetime
import sys
import os
import subprocess
import pprint as pp
import timeit

""" md5file = the abspath of the md5file generated in the original runfolder that have been copied into the backup runfolder."""

""" rf_path = the abspath of a backup runfolder """

def create_two_lists(rf_path):

    #The following creates a list of bam file and a list of bam.md5 files in the specified directory.
    
    assert os.path.exists(rf_path), "runfolder path DO NOT exist"
    assert os.path.isdir(create_org_runfolder), "runfolder path is NOT a directory"

    rf_path = os.path.abspath(rf_path)
    assert os.path.isabs(rf_path), "runfolder path NOT absolute"

    bam_list = []
    md5_list = []
    for root, dirname, filenames in os.walk(rf_path):
        for filename in filenames:
            #find all path to bam files
            if filename.endswith(".bam"):
                bam_list.append(os.path.join(root, filename))
            #find all path to md5 files associated with bam files
            if filename.split(".")[-2] == "bam" and filename.endswith(".md5"):
                md5_list.append(os.path.join(root, filename))

    create_list = sorted(bam_list)
    #print ("create_list:", create_list)
    check_list = sorted(md5_list)
    #print ("check_list:", check_list)
    
    return list(create_list), list(check_list)

def check_md5_exist(md5_path, rf_path):

    #check if the md5 file is present or not, if so record this in the md5_missing.txt log file.
         
    if os.path.exists(md5_path):
        print ("{} exist".format(md5_path))
        with open (os.path.join(rf_path, 'md5_missing.txt'), 'a') as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
        return True

    else:
        print ("{} file missing".format(md5_path))
        with open (os.path.join(rf_path, 'md5_missing.txt'), 'a') as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines('{} file missing\n'.format(md5_path))
            return False

def create_md5(create_list, rf_path):

    """For each bam file in the create_list, check if the md5 file exists. 
    If md5 associated with bam do not exist, create the md5 file"""
        
    for bam in create_list:
        if bam.endswith(".bam"):
            md5file = bam + ".md5"

            if check_md5_exist(md5file, rf_path):
                continue

            else:
                createmd5 = "md5sum {} > {}".format(bam, md5file)
                print ("creating a new md5 file: {}".format(md5file))
                subprocess.call(createmd5, shell=True)
                print ("new md5 file {} generated".format(md5file))
                with open (os.path.join(rf_path, 'md5_missing.txt'), 'a') as new_md5:
                    new_md5.writelines("time of generation: {}\n".format(datetime.datetime.now()))
                    new_md5.writelines('new md5 file {} generated\n'.format(md5file))

    return create_list

def create_logfile(rf_path):

    """create a log file in the specified directory called DATE.chk file"""

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    checkfilepath = os.path.abspath(checkfilepath)
    #print ("checkfilepath created")

    if os.path.exists(checkfilepath):
        print ('{} has already been checked today'.format(rf_path))

    else:
        createchk = "touch {}".format(checkfilepath)
        subprocess.call(createchk, shell=True)
        print ("check log {} generated".format(checkfilepath))

    return checkfilepath

def check_md5_hash(checkfilepath, md5, checksum):

    if len(checksum) == 32:
        #print ("{}: {} have 32 characters".format(md5, checksum))
        with open(checkfilepath, "a") as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("{}: {} have 32 characters\n".format(md5, checksum))
            return True

    else:
        print ("{}: {} DO NOT have 32 characters".format(md5))
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("{}: {} DO NOT have 32 characters\n".format(md5, checksum))
            return False    

def check_filename_match(checkfilepath, bam_filename, bam, md5):

    if bam == bam_filename:
        #print ("{} match {} in {}".format(bam_filename, bam, md5))
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("{} match {} in {}\n".format(bam_filename, bam, md5))
            return True
        
    else:
        print ("ERROR, mismatch found, {} DO NOT match {} in {}".format(bam_filename, bam, md5))
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("ERROR, mismatch found, {} DO NOT match {} in {}\n".format(bam_filename, bam, md5))
            return False

def check_md5_format(checkfilepath, check_list):
    
    """check the file integrity of bam files in the runfolder using md5sum -c for all the bam associated .md5 files in the check_list"""

    assert os.path.exists(checkfilepath), "checkfile path DO NOT exist"

    checkfilepath = os.path.abspath(checkfilepath)
    assert os.path.isabs(checkfilepath), "checkfile path NOT absolute"

    check_dict = {}

    for md5 in check_list:
        #print (md5)
        md5_filename = md5.split("/")[-1]
        #print (md5_filename)
        bam_filename = ".".join(md5.split("/")[-1].split(".")[:-1])
        #print (bam_filename)

        """check the format of md5 files in the check_list, if the format is correct, add the md5 and its hash into check_dict."""

        with open (md5) as md5_file:
            for line in md5_file:
                fields = line.strip().split("  ")
                checksum = fields[0]
                bam = fields[1].split("/")[-1]
                #print (bam)
                if check_md5_hash(checkfilepath, md5, checksum) and check_filename_match(checkfilepath, bam_filename, bam, md5) and md5_filename not in check_dict:
                    check_dict[md5_filename] = fields[0]

    return check_dict

def check_md5filename(rf_path, md5_filename, check_dict):

    """check if md5 file name is present in md5 check dictionary"""

    if md5_filename in check_dict:
        return True
    else:
        return False

def compare_md5hash(rf_path, md5_filename, check_dict):

    """check if md5 hash match between original and backup runfolder"""

    original_hash = check_dict["storage"][md5_filename]
    backup_hash = check_dict["archive"][md5_filename]

    if backup_hash == original_hash:
        return True
    else:
        return False

def check_hash_exist(rf_path, md5_filename, check_dict):

    """check if md5 hash exist in original or backup runfolder"""

    if check_dict["archive"][md5_filename] in check_dict["storage"].values():
        return True
    else:
        return False

    if check_dict["storage"][md5_filename] in check_dict["archive"].values():
        print ("{} hash in original folder found in backup folder".format(md5_filename))
        with open (os.path.join(rf_path, "md5_match.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            filename_check.writelines("{} hash in original folder found in backup folder\n".format(md5_filename))
            return True

    else:
        print ("{} hash in original folder NOT found in backup folder".format(md5_filename))
        with open (os.path.join(rf_path, "md5_mismatch.txt"), "a") as filename_check:
            filename_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            org_bkup_check.writelines("{} hash in original folder NOT found in backup folder\n".format(md5_filename))
            return False

def create_check_dict(orgfilepath, bkupfilepath, org_check_list, bkup_check_list):

    """create check_dict that includes hash and md5 file names from both original and backup runfolders"""
    assert os.path.exists(orgfilepath), "original checkfile path DO NOT exist"
    assert os.path.exists(bkupfilepath), "backup checkfile path DO NOT exist"
    
    orgfilepath = os.path.abspath(orgfilepath)
    assert os.path.isabs(orgfilepath), "original checkfile path NOT absolute"
    bkupfilepath = os.path.abspath(bkupfilepath)
    assert os.path.isabs(bkupfilepath), "backup checkfile path NOT absolute"

    check_dict = {}
    check_dict["storage"] = check_md5(orgfilepath, org_check_list)
    check_dict["archive"] = check_md5(bkupfilepath, bkup_check_list)

    return check_dict

def check_org_bkup(org_rf_path, bkup_rf_path, org_bkup_check_dict):

    assert os.path.exists(orf_rf_path), "original runfolder path DO NOT exist"
    assert os.path.exists(bkup_rf_path), "backup runfolder path DO NOT exist"
    org_rf_path = os.path.abspath(org_rf_path)
    assert os.path.isabs(org_rf_path), "original runfolder path NOT absolute"
    bkup_rf_path = os.path.abspath(bkup_rf_path)
    assert os.path.isabs(bkup_rf_path), "backup runfolder path NOT absolute"

    """check that .md5 in the original runfolder match that in the backup runfolder, 
    if the md5sum hash value do not match, or that the bam file name do not match,
    raise an error on terminal, and record the error in the error log"""

    #comments to explain what each dictionary stores 

    md5_matches = {} # dictionary of all md5s in original and backup runfolder with both filename and hash matching
    md5_matches["original"] = {} # nested dictionary of all md5s in original runfolder that matches backup
    md5_matches["backup"] = {} # nested dictionary of all md5s backup runfolder that matches original
    md5_mismatches = {} # dictionary of all md5s in original and backup runfolder that DO NOT match
    md5_mismatches["original"] = {} # nested dictionary of all md5s in original runfolder that DO NOT match backup
    md5_mismatches["backup"] = {} # nested dictionary of all md5s in backup runfolder that DO NOT match original
    md5_in_org_not_bkup = {} # dictionary of all md5s in original but NOT in backup
    md5_in_org_not_bkup["hash match"] = {} # nested dictionary of all md5 filenames in original runfolder but NOT backup with matching hash in backup
    md5_in_org_not_bkup["no hash match"] = {} # nested dictionary of all md5 filenames in original but NOT backup with NO matching hash in backup
    md5_in_bkup_not_org = {} # dictionary of all md5s in backup but NOT in original
    md5_in_bkup_not_org["hash match"] = {} # nested dictionary of all md5 filenames in backup runfolder but NOT original with matching hash in original
    md5_in_bkup_not_org["no hash match"] = {} # nested dictionary of all md5 filenames in backup runfolder but NOT original with matching in original

    print ("BACKUP vs ORIGINAL")

    for md5_filename in org_bkup_check_dict["archive"]:

        #comment on what each statement checks

        original_hash = check_dict["storage"][md5_filename]
        backup_hash = check_dict["archive"][md5_filename]

        with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            org_bkup_check.writelines("{} being checked\n".format(md5_filename))
        
        # if md5 filename present in backup and original, and md5 hash of both files match, add this to the md5_matches dictionary
        if check_md5filename(bkup_rf_path, md5_filename, org_bkup_check_dict["storage"]) and compare_md5hash(bkup_rf_path, md5_filename, org_bkup_check_dict):
            
            print ("{} present in {}".format(md5_filename, "original runfolder"))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} present {} \n".format(md5_filename), "original runfolder")

            print ("OK {} has matching hash".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as hash_check:
                hash_check.writelines("OK {} has matching hash \n".format(md5_filename))

            md5_matches["backup"][md5_filename] = org_bkup_check_dict["archive"][md5_filename]
            md5_matches["original"][md5_filename] = org_bkup_check_dict["storage"][md5_filename]
       
        # if md5 filename present in backup and original, but md5 hash do not match, add this to the md5_mismatches dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_bkup_check_dict["storage"]) and compare_md5hash(bkup_rf_path, md5_filename, org_bkup_check_dict) is False:
            
            print ("{} present in {}".format(md5_filename, "original runfolder"))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} present {} \n".format(md5_filename), "original runfolder")
            
            print ("ERROR, {} and {} in {} DO NOT match".format(backup_hash, original_hash, md5_filename))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as hash_check:
                hash_check.writelines("ERROR, {} and {} in {} DO NOT match\n".format(backup_hash, original_hash, md5_filename))

            md5_mismatches["backup"][md5_filename] = org_bkup_check_dict["archive"][md5_filename]
            md5_mismatches["original"][md5_filename] = org_bkup_check_dict["storage"][md5_filename]
        
        # if md5 filename present in backup, NOT in original, and hash of the file is present in backup, add this to md5_in_bkup_no_org["hash match"] dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_bkup_check_dict["storage"]) is False and check_hash_exist(bkup_path, md5_filename, org_bkup_check_dict):
            
            print ("ERROR, {} not present in {}".format(md5_filename, "original runfolder"))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("ERROR, {} not in {}\n".format(md5_filename, "original runfolder"))

            print ("{} hash in backup folder found in original folder".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} hash in backup folder found in original folder\n".format(md5_filename))

            md5_in_bkup_not_org["hash match"][md5_filename] = org_bkup_check_dict["archive"][md5_filename]
        
        # if md5 filename present in backup, NOT in original, and hash of the file is NOT present in backup, add this to md5_in_bkup_no_org["no hash match"] dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_bkup_check_dict["storage"]) is False and check_hash_exist(bkup_path, md5_filename, org_bkup_check_dict) is False:
            
            print ("ERROR, {} not present in {}".format(md5_filename, "original runfolder"))
            with open (os.path.join(rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("ERROR, {} not in {}\n".format(md5_filename, "original runfolder"))

            print ("{} hash in backup folder NOT found in original folder".format(md5_filename))
            with open (os.path.join(bkup_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} hash in backup folder NOT found in original folder\n".format(md5_filename))

            md5_in_bkup_not_org["no hash match"][md5_filename] = org_bkup_check_dict["archive"][md5_filename]

    print ("ORIGINAL vs BACKUP")

    for md5_filename in org_bkup_check_dict["storage"]:

        with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as org_bkup_check:
            org_bkup_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
            org_bkup_check.writelines("{} being checked\n".format(md5_filename))

        # if md5 filename present in backup, NOT in original, and hash of the file is present in backup, add this to md5_in_bkup_no_org["hash match"] dictionary
        if check_md5filename(org_rf_path, md5_filename, org_bkup_check_dict["archive"]) is False and check_hash_exist(org_path, md5_filename, org_bkup_check_dict):

            print ("ERROR, {} not present in {}".format(md5_filename, "backup runfolder"))
            with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("ERROR, {} not in {}\n".format(md5_filename, "backup runfolder"))

            print ("{} hash in backup folder found in original folder".format(md5_filename))
            with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} hash in backup folder found in original folder\n".format(md5_filename))

            md5_in_org_not_bkup["hash match"][md5_filename] = org_bkup_check_dict["storage"][md5_filename]
        
        # if md5 filename present in backup, NOT in original, and hash of the file is NOT present in backup, add this to md5_in_bkup_no_org["no hash match"] dictionary
        elif check_md5filename(org_rf_path, md5_filename, org_bkup_check_dict["archive"]) is False and check_hash_exist(org_path, md5_filename, org_bkup_check_dict) is False:
            
            print ("ERROR, {} not present in {}".format(md5_filename, "backup runfolder"))
            with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("ERROR, {} not in {}\n".format(md5_filename, "backup runfolder"))            

            print ("{} hash in backup folder NOT found in original folder".format(md5_filename))
            with open (os.path.join(org_rf_path, "org_bkup_check.txt"), "a") as filename_check:
                filename_check.writelines("{} hash in backup folder NOT found in original folder\n".format(md5_filename))

            md5_in_org_not_bkup["no hash match"][md5_filename] = org_bkup_check_dict["storage"][md5_filename]

    if md5_mismatches["original"] or md5_mismatches["backup"]:
        print "md5 mismatches found"
        pp.pprint(md5_mismatches)
    else:
        print "no md5 mismatch found"

    if md5_in_bkup_not_org["hash match"] or md5_in_bkup_not_org["no hash match"]:
        print "md5 in backup but not in original found"
        pp.pprint(md5_in_bkup_not_org)
    else:
        print "all backup .md5 present in original runfolder"

    if md5_in_org_not_bkup["hash match"] or md5_in_org_not_bkup["no hash match"]:
        print "md5 in original but not in backup found"
        pp.pprint(md5_in_org_not_bkup)
    else:
        print "all original .md5 present in backup runfolder"


def main(org_rf_path, bkup_rf_path, wkdir):

    wkdir = os.path.abspath(wkdir)
    org_rf_path = os.path.abspath(org_rf_path)
    bkup_rf_path = os.path.abspath(bkup_rf_path)

    #start timer
    start = timeit.default_timer()

    #generate a create_list and check_list for both original and backup runfolder
    org_create_list, org_check_list = create_two_lists(org_rf_path)
    bkup_create_list, bkup_check_list = create_two_lists(bkup_rf_path)

    #check bam files and md5 files exist in the runfolders
    #check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it.
    create_md5(org_create_list, org_rf_path)
    create_md5(bkup_create_list, bkup_rf_path)

    #create the check file path to log files
    orgfilepath = create_logfile(org_rf_path)
    bkupfilepath = create_logfile(bkup_rf_path)

    #check the md5 hash using md5sum sofware for each md5 file
    check_md5(orgfilepath, org_check_list)
    check_md5(bkupfilepath, bkup_check_list)

    #create a dictionary containing the md5 filenames and its associated md5 hash
    org_bkup_check_dict = create_check_dict(orgfilepath, bkupfilepath, org_check_list, bkup_check_list)

    #check md5sum values and bam filenames within .md5 match between original and backup runfolder
    check_org_bkup(org_rf_path, bkup_rf_path, org_bkup_check_dict)

    #end timer
    end = timeit.default_timer()

    timetaken = end - start
    print ("estimate of program run time:{}".format(timetaken))
    with open(os.path.join(wkdir, 'time.txt'), 'a') as time_text:
            time_text.writelines("time taken to check bam file integrity in {}\n and {}: {} \n".format(org_rf_path, bkup_rf_path, timetaken))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

#navigate to where the script is located from command line, and enter "python", then the name of the script "md5sumcript_5.py"

#followed by the original runfolder you wish to check - sys.argv[1]

#and the backup runfolder you wish to check - sys.argv[2]

#