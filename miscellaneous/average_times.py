#!usr/bin/python

"""Create a function to calculate the average processing time for checking file integrity of bam files."""

import sys
import pprint as pp
import os

def time_md5sum (timefile, rf_path):

    per_runfolder_times = []

    assert os.path.exists(timefile)

    """open md5_check.txt log file and find the line where the estimated program run time is recorded"""

    with open (timefile) as file_handle:
        for line in file_handle:
            # strip out the spaces at the end of each line.
            fields = line.strip()
            if "and" in fields and ":" in fields:
                fields = fields.split(" ")
                per_runfolder_times.append(fields[-1])

    """calculate the average time by taking the sum of all the estimated time and divide by the number of time the runfolder has been checked"""

    if len(per_runfolder_times) >= 1:
        per_runfolder_time = sum([float(x) for x in per_runfolder_times])/len(per_runfolder_times)
    else:
        per_runfolder_time = [float(x) for x in per_runfolder_times]
    
    """record the average time in the runfolder where the md5_check.txt log file is located, 
        when the runfolder has been checked multiple times, the script can be re-run to calculate new average time"""

    with open(os.path.join(rf_path, 'average_time.txt'), 'w+') as timetext:
        num_check = ""
        avg_time = ""
        if timetext.readline():                
            for line in timetext:
                if line.startswith("number"):
                    num_check = int(line.split(" ")[-1])
                    num_check += len(per_runfolder_times)
                elif line.startswith("average"):
                    avg_time = float(line.split(" ")[-1])
                    avg_time += per_runfolder_time
                else:
                    continue
            timetext.writelines("number of bams checked: {}\n average time taken to check {}: {}\n".format(len(num_check), rf_path, avg_time))
            print ("average time taken to check file integrity for {}: {}".format(rf_path, avg_time))

        else:
            timetext.writelines("number of bams checked: {}\n average time taken to check {}: {}\n".format(len(per_runfolder_times), rf_path, per_runfolder_time))
            print ("average time taken to check file integrity for {}: {}".format(rf_path, per_runfolder_time))
    
    return per_runfolder_times

def main(timefile1, timefile2):

    rf_path1 = os.path.dirname(os.path.abspath(timefile1))
    rf_path2 = os.path.dirname(os.path.abspath(timefile2))

    # call the function to print the number to terminal and save them in average_time.txt
    print ("original runfolder")
    time_md5sum(timefile1, rf_path1)
    print ("backup runfolder")
    time_md5sum(timefile2, rf_path2)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

"""From terminal navigate to the directory where the script is stored, 
    
    enter "python average_time.py", followed by the filepath to the md5_check.xtxt file to calculate the average time taken to check bam integrity
    e.g. /mnt/storage/home/zhengt/projects/md5sum/testrunfolders/test_000001_current_runfolder/time.txt"""
