#!usr/bin/python

import sys
import pprint
import md5sumscript
import create_bam_md5_lists
import os
import timeit

"""check all bam files integrity in the current NGS runfolders and backup NGS runfolders"""

def check_NGS_bam_md5(runfolders, rf_path)
    
    #identify all bams and md5s in the NGS folders
    
    #generate a nested dictionary containing runfolder, bam and md5 files in the NGS folders. 
    bam_md5_dict = check_bam_md5_runfolders.create_bam_md5_dict(runfolders, rf_path)
    
    #use the generated dictionary above, create a list of all bams without md5, a list of md5 with bam, and a list of md5 without bam
    bam_without_md5, md5_with_bam, md5_without_bam = create_bam_md5_lists.create_bam_md5_lists(bam_md5_dict, rf_path)
    
    #create the check and error log files
    checkfilepath, errorfilepath = md5sumscript.create_logfiles(rf_path)

    #check all the md5s in both md5_with_bam and md5_without_bam
    md5_list = md5_with_bam + md5_without_bam
    md5sumscript.check_md5(rf_path,checkfilepath, errorfilepath, md5_list)

    #generate .md5 for bams without .md5
    md5sumscript.create_md5(bam_without_md5, rf_path)
    
    return md5_list

def main(original, backup, rf_path):
    
    #start timer
    start = timeit.default_timer()

    #indicate where the check logs and error logs for the check will be stored"
    rf_path = os.path.abspath(rf_path)
    print ("directory where check log files will be stored:", rf_path)

    #check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it.
    create_md5(org_create_list, org_rf_path)
    create_md5(bkup_create_list, bkup_rf_path)

    #execute function to check all bams and md5s in original and backup NGS runfolders
    check_list_original = check_NGS_bam_md5(original, rf_path)
    check_list_backup = check_NGS_bam_md5(backup, rf_path)
    md5sumscript.check_org_bkup(rf_path, check_list_original, check_list_backup)

    print ("check all bam and md5 files in NGS runfolders complete")

    #end timer
    end = timeit.default_timer()
    time_taken = end - start
    with open(os.path.join(db_dir, 'time.txt'), 'a') as time_text:
            time_text.writelines("time taken to check md5sums for all NGS runfolders : {} \n".format(time_taken))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    
"""From terminal navigate to the directory where the script is stored, 
    
    enter "python check_all_bams.py", followed by the original NGS runfolders - sys.argv[1] 
    e.g. /mnt/storage/data/NGS/

    and the backup NGS runfolders - sys.argv[2] 
    e.g. /mnt/archive/data/NGS/"""