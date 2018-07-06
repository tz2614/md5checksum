#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re

# md5file = the abspath of the md5file generated in the original runfolder that have been copied into the backup runfolder.

# rf = the abspath of backup runfolder 

def main(rf):

    #rf_name_1stpart = rf.split("_")[0]
    #rf_name_lastpart = rf.split("_")[-1]
    #assert re.match(r'[0-9]', rf_name_1stpart), "first part of runfolder name did not match"
    #assert re.match(r'[A-Z][0-9]', rf_name_lastpart), "last part of runfolder name did not match"

    rf_path = os.path.abspath(rf)

    checkfile = str(datetime.datetime.now()).split(" ")[0] + ".chk"
    checkfilepath = os.path.join(rf_path, checkfile)

    errorfile = str(datetime.datetime.now()).split(" ")[0] + ".err"
    errorfilepath = os.path.join(rf_path, errorfile)

    bam_list = sorted(glob.glob("{}/bams/*.bam".format(str(rf_path))))
    vcf_list = sorted(glob.glob("{}/vcfs/*.vcf".format(str(rf_path))))
    otherfile_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))
    md5_list = bam_list + vcf_list + otherfile_list
    filetoexclude = ["md5", "chk", "err"]

    md5_list = [x for x in md5_list if x.split(".")[-1] not in filetoexclude]

    if os.path.exists(checkfilepath):
        print 'This folder has already been checked today'
        exit()
    
    else:
        createchk = "touch /{}".format(checkfilepath)
        #print createchk
        subprocess.call(createchk, shell=True)
        createerr = "touch /{}".format(errorfilepath)
        #print createerr
        subprocess.call(createerr, shell=True)

    for md5 in md5_list:
        md5file = md5 + ".md5"
        #print md5file 
        
        if not os.path.exists(md5file):
            print "md5file for {} do not exist".format(md5)
            continue
        else:

            md5chk = "md5sum -c {} >> {} 2>> {}".format(md5file, checkfilepath, errorfilepath)
            #print md5chk
            subprocess.call(md5chk, shell=True)

    """if not md5file:
            print 'The md5file do not exist, creating a new md5file'
            createmd5 = "md5sum rf/*.bam /vcfs/*.vcf *.vcf > hash.md5"
            subprocess.call(createmd5, shell=True)
            copymd5 = "cp rf/hash.md5 > destination/md5file"
            subprocess.call(copymd5, shell=True) """

        #copy=sh.awk("'{print $1}'hash.md5")

        #original=sh.awk("'{print $1}'filepath/hash.md5")
    
        #if copy == original:
            #checkfile.append("file integrity intact\n")
            #continue
        #else:
            #checkfile.append("file integrity compromised\n")

def createmd5(rf):
    rf_path = os.path.abspath(rf)
    bam_list = sorted(glob.glob("{}/bams/*.bam".format(str(rf_path))))
    #print bam_list
    vcf_list = sorted(glob.glob("{}/vcfs/*.vcf".format(str(rf_path))))
    #print vcf_list
    otherfile_list = sorted(glob.glob("{}/*.*".format(str(rf_path))))
    all_list = bam_list + vcf_list + otherfile_list
    #print all_list

    filetoexclude = [".md5", ".chk", ".err"]

    for md5 in all_list:
        #print md5
        if any ([md5.endswith(x) for x in filetoexclude]):
            continue

        else:
            md5file = md5 + ".md5"
            #print md5file
        
        if not os.path.exists(md5file):
            print 'The md5file do not exist, creating a new md5file'
            createmd5 = "md5sum {} > {}".format(md5, md5file)
            subprocess.call(createmd5, shell=True)

if __name__ == "__main__":
    main(sys.argv[1])
    createmd5(sys.argv[1])