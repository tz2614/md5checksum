#!usr/bin/python

from __future__ import print_function
import sys
import glob
import os
import datetime
import subprocess
import pprint as pp

def missing_md5_list(storage, wkdir):

    #identify all bam files in the gemini folder and assign it to bam_list
    
    #1. apply a regular expression pattern matching to identify all runfolders that contain the gemini runs.
    #2. place all runfolder into a unique set of list.
    #3. iterate through the list to find all bam files and append the path to the file in a text file.

    assert (storage == "/mnt/storage/data/NGS" or storage == "/mnt/storage/data/NGS/"), "runfolder given incorrect"
    runfolder_pattern = "{}/*/*/[0-9][0-9][0-9][0-9][0-9][0-9]_*/bams/".format(str(storage))
    
    #generate a list of filepath to the runfolders containing bam, md5 files in the geminifolder. 

    runfolder_list = list(sorted(set(glob.glob(runfolder_pattern))))
    #print (runfolder_list)
    #print (bam_list)
    #print (md5_list)

    bam_md5_dict = {}

    for runfolder in runfolder_list:
        
        new_md5_list = []
        new_bam_list = []
        bam_md5_dict[runfolder] = {}
    
    # creating a nested dictionary containing runfolder as keys, associated list of bam/md5 filenames as values in a nested dictionary
        for root, dirname, filenames in os.walk(runfolder):
            for filename in filenames:
                if filename.endswith(".md5"):
                    new_md5_list.append(filename)
                if filename.endswith(".bam"):
                    new_bam_list.append(filename)

        #print (new_md5_list)
        #print (new_bam_list)

        bam_md5_dict[runfolder]["md5"] = new_md5_list
        bam_md5_dict[runfolder]["bam"] = new_bam_list

    #pp.pprint(bam_md5_dict)

    # if bam filename in md5 filename list, then we know there is a matching md5 with the bam, create two textfile lists. one bam with md5, one bam without md5.
    for runfolder in runfolder_list:
        print ("runfolder being checked :", runfolder)
        bam_files = bam_md5_dict[runfolder]["bam"]
        for bam_file in bam_files:
            bam_md5 = bam_file + ".md5"
            if bam_md5 in bam_md5_dict[runfolder]["md5"]:
                print ('md5 for {} is present'.format(bam_file))
                with open(os.path.join(wkdir,'bam_with_md5.txt'), 'a') as good_bam:
                    bam_file = os.path.abspath(runfolder) + "/" + bam_file
                    good_bam.writelines('{}\n'.format(bam_file))
            else:
                #bam_list_with_md5.append(bam)
                print ('md5 for {} is missing'.format(bam_file))
                with open(os.path.join(wkdir,'bam_err_list.txt'), 'a') as bad_bam:
                    bam_file = os.path.abspath(runfolder) + "/" + bam_file
                    bad_bam.writelines('{}\n'.format(bam_file))

    with open(os.path.join(wkdir, "bam_with_md5.txt"), "a") as good_bam:
        good_bam.writelines('date of this check: {}\n'.format(datetime.datetime.now()))

    with open(os.path.join(wkdir, "bam_err_list.txt"), "a") as bad_bam:
        bad_bam.writelines('date of this check: {}\n'.format(datetime.datetime.now()))

    # if md5 filename not in bam filename list, create a list of md5, where the bam is missing.
        md5_files = bam_md5_dict[runfolder]["md5"]
        for md5_file in md5_files:
            md5_file = md5_file.split(".")
            md5_bam = md5_file[0] + ".bam"
            if md5_bam not in bam_md5_dict[runfolder]["bam"]:
                print ('bam for {} is missing'.format(md5_file))
                with open(os.path.join(wkdir,'md5_err_list.txt'), 'a') as bad_md5:
                    md5_file = os.path.abspath(runfolder) + "/" + md5_file
                    bad_md5.writelines('bam for {} is missing \n'.format(md5_file))
    
    with open(os.path.join(wkdir, "md5_err_list.txt"), "a") as bad_md5:
        bad_md5.writelines('date of this check: {}\n'.format(datetime.datetime.now()))

    return bam_md5_dict
        
def main(storage, wkdir):
    storage = os.path.abspath(storage)
    print ("storage directory currently being checked: ", storage)
    wkdir = os.path.abspath(wkdir)
    print ("directory where the list of bams/md5 is stored: ", wkdir)
    #execute function to find a list of bam files missing md5
    missing_md5_list(storage, wkdir)
    print ("all bam files checked for associated md5 file")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    
#from command line enter "python", then the name of the script "check_missing_md5files.py"

#followed by the directory containing all bams you wish to check - sys.argv[1]

#specify the directory where the list of files missing md5 will be created - sys.argv[2]
