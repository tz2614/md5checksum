#!usr/bin/python2

import datetime
import sys
import os
import subprocess
import pprint as pp
import timeit


"""
This program is designed to check the file integrity of bam files within a NGS runfolder, 
and compare that with the bam files in the same runfolder in backup. 

The program takes two arguments, one is the runfolder path to a specific runfolder 
e.g. /mnt/storage/data/NGS/123456_K00178/

the other is the runfolder path to the same runfolder but in the backup directory
e.g. /mnt/storage/data/NGS/123456_K00178/


The program obtains a list of all the bam files and a list of associated md5s that are present in the directory via the create_two_lists() function.
--> create_list, check_list.

If the md5 for a particular bam file is missing, the create_md5() function will generate the md5 for that particular bam file.

The program then checks the format of all the associated md5s, and compares its hash against one generated afresh using md5sum -c program via the check_md5() function.

This gives an indication of whether a particular bam file is corrupted or not.
If the check is "OK", then the file is intact, if the check returns "ERROR, ..." then this will need to be investigated, the output from md5sum -c program is recorded in the DATE.chk log in the runfolder specified.

A dictionary containing the md5 filename and its associated hash in both original and backup runfolder is then created via the function
create_check_dict()

Any mismatches in the md5 checksum or md5 filename between the backup and original bam is recorded in org_bkup_check.txt log files within the original runfolder.

"""

# inputs and outputs of functions

# create_list = a list of absolute file path to bam files in the specified runfolder

# check_list = a list of md5_path associated with bam files in the specified runfolder

# md5_path = the absolute filepath to a md5 file in the specified runfolder.

# rf_path = the absolute filepath of a particular runfolder

# checkfilepath = the absolute filepath to the DATE.chk log file, which stores the output from the md5sum -c program

# new_md5_list = a list of md5_path that have been newly created via the create_md5() function

# md5_filename = the md5 filename extracted from the md5_path

# check_dict = dictionary of md5 filenames and md5 hash values created from check_md5() 

# org_bkup_dict = nested dictionary containing two nested dictionaries, one is "storage", the other is "archived". Each of these sub-dictionary contain md5 filenames and md5 hash values from check_dict

# md5_matches, md5_mismatches, md5_in_org_not_bkup, md5_in_bkup_not_org = four dictionaries created from org_bkup_check() showing matches and mismatches between original and backup runfolder

def create_two_lists(rf_path):

    #The following creates a list of bam file and a list of bam.md5 files in the specified directory.

    rf_path = os.path.abspath(rf_path)
    assert os.path.isabs(rf_path), "{} NOT absolute".format(rf_path)
    assert os.path.exists(rf_path), "{} DO NOT exist".format(rf_path)
    assert os.path.isdir(rf_path), "{} is NOT a directory".format(rf_path)

    bam_list = []
    md5_list = []
    for root, dirname, filenames in os.walk(rf_path):
        for filename in filenames:
            #find all path to bam files
            if filename.endswith(".bam"):
                bam_list.append(os.path.join(root, filename))
            #find all path to md5 files associated with bam files
            if filename.endswith(".md5") and filename.split(".")[-2] == "bam":
                md5_list.append(os.path.join(root, filename))

    create_list = sorted(bam_list)
    #print ("create_list:", create_list)
    check_list = sorted(md5_list)
    #print ("check_list:", check_list)
    
    return create_list, check_list

def check_md5_exist(md5_path, rf_path):

    #check if the md5 file is present or not, if the md5 file is missing record this in the md5_check.txt log file.

        if os.path.exists(md5_path):
            with open (os.path.join(rf_path, "md5_check.txt"), 'a') as md5_check:
                md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
                md5_check.writelines('{} present\n'.format(md5_path))
            return True

        else:
            with open (os.path.join(rf_path, "md5_check.txt"), 'a') as md5_check:
                md5_check.writelines("time of check: {}\n".format(datetime.datetime.now()))
                md5_check.writelines('{} missing\n'.format(md5_path))
            return False

def create_md5(create_list, rf_path):

    """check the bam.md5 list, and see if each bam.md5 file exist. 
    If md5 associated with bam do not exist, create the md5 file"""

    assert type(create_list) is list, "bam list provided is NOT a list"
    assert create_list, "bam list is empty, no bam files present in {}".format(rf_path)
    for path in create_list:
        assert os.path.exists(path), "{} in bam list DO NOT exist".format(path)
    
    new_md5_list = []
       
    for bam in create_list:
        if bam.endswith(".bam"):
            md5file = bam + ".md5"

        if check_md5_exist(md5file, rf_path):
            continue

        else:
            bam = bam.split("/")[-1]
            md5 = bam + ".md5"
            createmd5 = "cd {}; md5sum {} > {}".format(rf_path, bam, md5)
            print ("creating a new md5 file: {}".format(md5))
            subprocess.call(createmd5, shell=True)
            print ("new md5 file {} generated".format(md5file))
            new_md5_list.append(md5file)
            with open (os.path.join(rf_path, "md5_check.txt"), 'a') as new_md5:
                new_md5.writelines('new md5 file {} generated\n'.format(md5file))
                new_md5.writelines("time of generation: {}\n".format(datetime.datetime.now()))

    if new_md5_list != []:
        print "list of new md5s generated: {}".format(new_md5_list)
    
    return new_md5_list

def create_logfile(rf_path):

    """create a log file in the specified runfolder called DATE.chk file, where DATE is in the format YYYY-MM-DD"""

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)
    checkfilepath = os.path.abspath(checkfilepath)

    if os.path.exists(checkfilepath):
        print ('{} has already been checked today'.format(rf_path))

    else:
        createchk = "touch {}".format(checkfilepath)
        subprocess.call(createchk, shell=True)

    return checkfilepath

def check_md5_hash(checkfilepath, md5_filename, checksum):

    """Check the md5 hash in the md5 file has correct length and consist of either letters or numbers"""

    if len(checksum) == 32 and checksum.isalnum():
        with open(checkfilepath, "a") as md5_check:
            md5_check.writelines("time of hash check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("OK, {}: {} md5 hash in correct format\n".format(md5_filename, checksum))
        return True

    else:
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of hash check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("ERROR, {}: {} md5 hash NOT in correct format\n".format(md5_filename, checksum))
        return False

def check_filename(checkfilepath, bam_filename, bam, md5):

    # Check the bam filename match the one in the .md5 file.

    if bam_filename == bam:
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of filename check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("OK, bam filename {} match {} in {}\n\n".format(bam, bam_filename, md5))
        return True
        
    else:
        with open (checkfilepath, "a") as md5_check:
            md5_check.writelines("time of filename check: {}\n".format(datetime.datetime.now()))
            md5_check.writelines("ERROR, bam filename {} DO NOT match {} in {}\n\n".format(bam_filename, bam, md5))
        return False

def check_md5(checkfilepath, check_list):

    """check the format of md5 files in the check_list, record the errors in the checkfilepath, 
    then add the md5 filename and its hash into a dictionary called check_dict."""

    assert os.path.exists(checkfilepath), "checkfile path DO NOT exist"
    
    assert type(check_list) is list, "bam.md5 list provided is NOT a list"

    for path in check_list:
        assert os.path.exists(path), "{} in md5 list DO NOT exist".format(path)
    for path in check_list:
        assert os.path.isabs(path), "{} in md5 list is not an absolute path".format(path)

    check_dict = {}
    md5_bam_dict = {}

    for md5 in check_list:

        md5_filename = md5.split("/")[-1]
    
        bam_filename = ".".join(md5_filename.split(".")[:-1])
    
        rf_path = "/".join(md5.split("/")[:-1])

        print ("{} file is being checked".format(md5))

        """using md5sum -c, read md5 sums from .md5 files and check if they match those generated by the md5sum program"""

        with open (checkfilepath, 'a') as md5_check:
            md5chk = "cd {}; md5sum -c {} >> {} 2>> {}".format(rf_path, md5_filename, checkfilepath, checkfilepath)
            chk_output = subprocess.call(md5chk, shell=True)
    
        if md5_filename not in check_dict:

            with open (md5, "r") as md5_file:

                line = md5_file.readline().strip()
                if line == '':
                    checksum = "NONE"
                    bam = "NONE"
                    check_md5_hash(checkfilepath, md5, checksum)
                    check_filename(checkfilepath, bam_filename, bam, md5)
                    md5_bam_dict[md5_filename] = bam
                    check_dict[md5_filename] = checksum

                elif line[32:] == '':
                    bam = "NONE"
                    checksum = line[:32]
                    check_md5_hash(checkfilepath, md5, checksum)
                    check_filename(checkfilepath, bam_filename, bam, md5)
                    md5_bam_dict[md5_filename] = bam
                    check_dict[md5_filename] = checksum

                elif line[:32] == '':
                    bam = line[32:].split("/")[-1]
                    checksum = "NONE"
                    check_md5_hash(checkfilepath, md5, checksum)
                    check_filename(checkfilepath, bam_filename, bam, md5)
                    md5_bam_dict[md5_filename] = bam
                    check_dict[md5_filename] = checksum

                else:
                    fields = line.split("  ")

                    if len(fields) == 2:
                        bam = fields[-1].split("/")[-1]
                        checksum = fields[0]
                        if bam == '':
                            bam = "NONE"
                        if checksum == '':
                            checksum = "NONE"
                        check_md5_hash(checkfilepath, md5_filename, checksum)
                        check_filename(checkfilepath, bam_filename, bam, md5)
                        md5_bam_dict[md5_filename] = bam
                        check_dict[md5_filename] = checksum                           

    return check_dict, md5_bam_dict

def check_md5filename(rf_path, md5_filename, check_dict):

    """check if md5 file name is present in md5 check dictionary"""

    if md5_filename in check_dict:
        return True
    else:
        return False

def compare_md5hash(original_hash, backup_hash):

    """check if md5 hash match between original and backup runfolder"""

    if backup_hash == original_hash:
        return True
    else:
        return False

def check_hash_exist(md5_filename, check_dict1, check_dict2):

    """check if md5 hash exist in check_dict specified"""

    if check_dict1[md5_filename] in check_dict2.values():
        return True
    
    else:
        return False

def check_org_bkup(org_rf_path, bkup_rf_path, org_checkfilepath, bkup_checkfilepath, org_check_dict, bkup_check_dict):

    """check that .md5 in the original runfolder match that in the backup runfolder, 
    if the md5sum hash value do not match, or that the bam file name do not match,
    raise an error on terminal, and record the error in the error log"""

    # check org_bkup_check_dict is a dictionary
    assert type(org_check_dict) is dict, "the nested dictionary containing original md5s is not a dictionary"
    assert type(bkup_check_dict) is dict, "the nested dictionary containing backup md5s is not a dictionary"

    # dictionary of all md5s in original and backup runfolder with both filename and hash matching
    md5_matches = {} 

    # nested dictionary of all md5s in original runfolder that matches backup
    md5_matches["original"] = {}

    # nested dictionary of all md5s backup runfolder that matches original 
    md5_matches["backup"] = {} 

    # dictionary of all md5s in original and backup runfolder that DO NOT match
    md5_mismatches = {} 

    # nested dictionary of all md5s in original runfolder that DO NOT match backup
    md5_mismatches["original"] = {} 

    # nested dictionary of all md5s in backup runfolder that DO NOT match original
    md5_mismatches["backup"] = {} 

    # dictionary of all md5s in original but NOT in backup
    md5_in_org_not_bkup = {} 

    # nested dictionary of all md5 filenames in original runfolder but NOT backup with matching hash in backup
    md5_in_org_not_bkup["hash present"] = {} 

    # nested dictionary of all md5 filenames in original runfolder but NOT backup with NO matching hash in backup
    md5_in_org_not_bkup["no hash match"] = {} 
    
    # dictionary of all md5s in backup but NOT in original
    md5_in_bkup_not_org = {} 
    
    # nested dictionary of all md5 filenames in backup runfolder but NOT original with matching hash in original
    md5_in_bkup_not_org["hash present"] = {} 
    
    # nested dictionary of all md5 filenames in backup runfolder but NOT original with NO matching hash in original
    md5_in_bkup_not_org["no hash match"] = {} 

    print ("BACKUP vs ORIGINAL\n")
    with open (bkup_checkfilepath, "a") as bkup_check:
        bkup_check.writelines("BACKUP vs ORIGINAL\n\n")
        bkup_check.writelines("time of check: {}\n".format(datetime.datetime.now()))

    for md5_filename in bkup_check_dict:

        if md5_filename in org_check_dict:
            original_hash = org_check_dict[md5_filename]
            backup_hash = bkup_check_dict[md5_filename]
        else:
            backup_hash = bkup_check_dict[md5_filename]
            original_hash = "NONE"

        print ("{} being checked".format(md5_filename))
        with open (bkup_checkfilepath, "a") as bkup_check:
            bkup_check.writelines("{} being checked\n".format(md5_filename))
        
        # if md5 filename present in backup and original, and md5 hash of both files match, add this to the md5_matches dictionary
        if check_md5filename(bkup_rf_path, md5_filename, org_check_dict) is True and compare_md5hash(original_hash, backup_hash) is True:
            
            with open (bkup_checkfilepath, "a") as bkup_check:
            
                bkup_check.writelines("OK, {} present in backup and original runfolder\n".format(md5_filename))
                bkup_check.writelines("OK, {} has matching hash\n".format(md5_filename))

            md5_matches["backup"][md5_filename] = bkup_check_dict[md5_filename]
       
        # if md5 filename present in backup and original, but md5 hash do not match, add this to the md5_mismatches dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_check_dict) is True and compare_md5hash(original_hash, backup_hash) is False:
            
            with open (bkup_checkfilepath, "a") as bkup_check:
                
                bkup_check.writelines("OK, {} present in backup and original runfolder\n".format(md5_filename))
                bkup_check.writelines("ERROR, {} and {} in {} DO NOT match\n".format(backup_hash, original_hash, md5_filename))

            md5_mismatches["backup"][md5_filename] = bkup_check_dict[md5_filename]
        
        # if md5 filename present in backup, NOT in original, and hash of the file is present in original, add this to md5_in_bkup_not_org["hash present"] dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_check_dict) is False and check_hash_exist(md5_filename, bkup_check_dict, org_check_dict) is True:
            
            with open (bkup_checkfilepath, "a") as bkup_check:

                bkup_check.writelines("ERROR, {} not present in original runfolder\n".format(md5_filename))
                bkup_check.writelines("{} hash in backup folder found in original folder\n".format(md5_filename))

            md5_in_bkup_not_org["hash present"][md5_filename] = bkup_check_dict[md5_filename]
        
        # if md5 filename present in backup, NOT in original, and hash of the file is NOT present in original, add this to md5_in_bkup_not_org["no hash match"] dictionary
        elif check_md5filename(bkup_rf_path, md5_filename, org_check_dict) is False and check_hash_exist(md5_filename, bkup_check_dict, org_check_dict) is False:
            
            with open (bkup_checkfilepath, "a") as bkup_check:

                bkup_check.writelines("ERROR, {} not in original runfolder\n".format(md5_filename))
                bkup_check.writelines("{} hash in backup folder NOT found in original folder\n".format(md5_filename))

            md5_in_bkup_not_org["no hash match"][md5_filename] = bkup_check_dict[md5_filename]

    print
    print ("ORIGINAL vs BACKUP\n")
    with open (org_checkfilepath, "a") as org_check:
        org_check.writelines("ORIGINAL vs BACKUP\n\n")
        org_check.writelines("time of check: {}\n".format(datetime.datetime.now()))

    for md5_filename in org_check_dict:

        if md5_filename in bkup_check_dict:
            backup_hash = bkup_check_dict[md5_filename]
            original_hash = org_check_dict[md5_filename]
        else:
            original_hash = org_check_dict[md5_filename]
            backup_hash = "NONE"

        print ("{} being checked".format(md5_filename))
        with open (org_checkfilepath, "a") as org_check:
            org_check.writelines("{} being checked\n".format(md5_filename))

        # if md5 filename present in original and backup, and md5 hash of both files match, add this to the md5_matches dictionary
        if check_md5filename(org_rf_path, md5_filename, bkup_check_dict) is True and compare_md5hash(original_hash, backup_hash) is True:

            with open (org_checkfilepath, "a") as org_check:
                
                org_check.writelines("OK, {} present in original and backup runfolder\n".format(md5_filename))
                org_check.writelines("OK, {} has matching hash\n".format(md5_filename))

            md5_matches["original"][md5_filename] = org_check_dict[md5_filename]

        # if md5 filename present in original and backup, but md5 hash do not match, add this to the md5_mismatches dictionary
        elif check_md5filename(org_rf_path, md5_filename, bkup_check_dict) is True and compare_md5hash(original_hash, backup_hash) is False:
            
            with open (org_checkfilepath, "a") as org_check:
    
                org_check.writelines("OK, {} present in backup and original runfolder\n".format(md5_filename))
                org_check.writelines("ERROR, {} and {} in {} DO NOT match\n".format(backup_hash, original_hash, md5_filename))

            md5_mismatches["original"][md5_filename] = org_check_dict[md5_filename]

        # if md5 filename present in original, NOT in backup, and hash of the file is present in backup, add this to md5_in_org_not_bkup["hash present"] dictionary
        if check_md5filename(org_rf_path, md5_filename, bkup_check_dict) is False and check_hash_exist(md5_filename, org_check_dict, bkup_check_dict) is True:
            
            with open (org_checkfilepath, "a") as org_check:

                org_check.writelines("ERROR, {} not in backup runfolder\n".format(md5_filename))
                org_check.writelines("{} hash in backup folder found in original folder\n".format(md5_filename))

            md5_in_org_not_bkup["hash present"][md5_filename] = org_check_dict[md5_filename]
        
        # if md5 filename present in original, NOT in backup, and hash of the file is NOT present in backup, add this to md5_in_org_not_bkup["no hash match"] dictionary
        elif check_md5filename(org_rf_path, md5_filename, bkup_check_dict) is False and check_hash_exist(md5_filename, org_check_dict, bkup_check_dict) is False:
            
            with open (org_checkfilepath, "a") as org_check:

                org_check.writelines("ERROR, {} not in backup runfolder\n".format(md5_filename))            
                org_check.writelines("{} hash in backup folder NOT found in original folder\n".format(md5_filename))

            md5_in_org_not_bkup["no hash match"][md5_filename] = org_check_dict[md5_filename]

    print

    if md5_matches["original"] or md5_matches["backup"]:
        print ("md5 matches found")
        pp.pprint(md5_matches)
    else:
        print ("no md5 matches found")

    if md5_mismatches["original"] or md5_mismatches["backup"]:
        print ("md5 mismatches found")
        pp.pprint(md5_mismatches)
    else:
        print ("no md5 mismatch found")

    if md5_in_bkup_not_org["hash present"] or md5_in_bkup_not_org["no hash match"]:
        print ("md5 in backup but not in original found")
        pp.pprint(md5_in_bkup_not_org)
    else:
        print ("all backup .md5 present in original runfolder")

    if md5_in_org_not_bkup["hash present"] or md5_in_org_not_bkup["no hash match"]:
        print "md5 in original but not in backup found"
        pp.pprint(md5_in_org_not_bkup)
    else:
        print ("all original .md5 present in backup runfolder")

    return md5_matches, md5_mismatches, md5_in_org_not_bkup, md5_in_bkup_not_org

def main(org_rf_path, bkup_rf_path):

    #wkdir = "/mnt/storage/home/zhengt/projects/md5checksum/"
    org_rf_path = os.path.abspath(org_rf_path)
    #assert org_rf_path.startswith("/mnt/storage/"), "original runfolder given NOT from /mnt/storage"
    bkup_rf_path = os.path.abspath(bkup_rf_path)
    #assert org_bkup_path.startswith("/mnt/archive/"), "backup runfolder given NOT from /mnt/archive"

    #start timer
    start = timeit.default_timer()

    #generate a create_list and check_list for both original and backup runfolder
    org_create_list, org_check_list = create_two_lists(org_rf_path)
    bkup_create_list, bkup_check_list = create_two_lists(bkup_rf_path)

    #check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it.
    new_md5_list_in_org = create_md5(org_create_list, org_rf_path)
    new_md5_list_in_bkup = create_md5(bkup_create_list, bkup_rf_path)

    new_check_list_in_org = org_check_list + new_md5_list_in_org
    new_check_list_in_bkup = bkup_check_list + new_md5_list_in_bkup

    #create the log files and return the file paths
    org_checkfilepath = create_logfile(org_rf_path)
    bkup_checkfilepath = create_logfile(bkup_rf_path)

    try:
        with open(org_checkfilepath, "a") as check_file:
            check_file.writelines("testing")
    except PermissionError:
        org_checkfilepath = create_logfile(input('Enter a directory where you have write permission to write to store the log file e.g./mnt//storage/home/zhengt/md5checksum/'))
        assert os.path.exists(org_checkfilepath), "path given DO NOT exist, try another"

    try:
        with open(bkup_checkfilepath, "a") as check_file:
            check_file.writelines("testing")
    except PermissionError:
        bkup_checkfilepath = create_logfile(input('Enter a directory where you have write permission to stor the log file e.g./mnt//storage/home/zhengt/md5checksum/'))
        assert os.path.exists(bkup_checkfilepath), "path given DO NOT exist, try another"

    #create a dictionary containing the md5 filenames and its associated md5 hash for backup and original runfolder
    org_check_dict, org_md5_bam_dict = check_md5(org_checkfilepath, new_check_list_in_org)
    bkup_check_dict, bkup_md5_bam_dict = check_md5(bkup_checkfilepath, new_check_list_in_bkup)
    print

    #check md5sum values and bam filenames within .md5 match between original and backup runfolder for the existing md5s in org_check_dict1 and new md5s in org_check_dict2
    check_org_bkup(org_rf_path, bkup_rf_path, org_checkfilepath, bkup_checkfilepath, org_check_dict, bkup_check_dict)
    print

    #create a list of md5_filenames as input to the final md5_table
    common_md5_filenames = list(set(org_md5_bam_dict.keys() + bkup_md5_bam_dict.keys()))
    unique_org_md5_filenames = set(org_md5_bam_dict.keys())
    unique_bkup_md5_filenames = set(bkup_md5_bam_dict.keys())
    unique_md5_filenames = list(unique_org_md5_filenames ^ unique_bkup_md5_filenames)
    md5_filenames = sorted(common_md5_filenames + unique_md5_filenames)

    # use plotly to create a table containing all the md5s, associated bam filenames and md5 hash for the runfolders provided.
    from plotly.offline import plot
    import plotly.graph_objs as go

    trace = go.Table(
        header=dict(values=['md5 filename', 'bam filename(original)', 'bam filename(backup)', 'md5_hash(original)', 'md5_hash(backup)'],
                    line = dict(color='#000000'),
                    fill = dict(color='#E6E6FA'),
                    align = ['left'] * 5),
        cells=dict(values=[[md5 for md5 in md5_filenames], [org_md5_bam_dict[md5] for md5 in org_md5_bam_dict.keys()], 
                            [bkup_md5_bam_dict[md5] for md5 in bkup_md5_bam_dict.keys()],
                            [org_check_dict[md5] for md5 in org_check_dict.keys()], 
                            [bkup_check_dict[md5] for md5 in bkup_check_dict.keys()]],
                   line = dict(color='#000000'),
                   fill = dict(color='#FFFFFF'),
                   align = ['left'] * 5))

    layout = go.Layout(
        title="{} and {}".format(org_rf_path, bkup_rf_path))
    data = [trace]
    fig = dict(data=data, layout=layout)
    plot(fig, filename ="md5_table.html")

    #end timer
    end = timeit.default_timer()

    timetaken = end - start
    print ("estimate of program run time:{}".format(timetaken))
    with open(org_checkfilepath, 'a') as time_text:
        time_text.writelines("time taken to check bam files integrity in {}\n and {}: {} \n\n".format(org_rf_path, bkup_rf_path, timetaken))
    with open(bkup_checkfilepath, 'a') as time_text:
        time_text.writelines("time taken to check bam files integrity in {}\n and {}: {} \n\n".format(org_rf_path, bkup_rf_path, timetaken))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

#navigate to where the script is located from command line, and enter "python", then the name of the script "md5sumcript.py"

#followed by the original runfolder you wish to check - sys.argv[1]

#and the backup runfolder you wish to check - sys.argv[2]