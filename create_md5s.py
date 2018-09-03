#!usr/bin/python

import sys
import pprint
import md5sumscript_5
import os

    """check the create_list of bam files to see if .md5 files for each bam file is present, if not generate it."""

def main(runfolders, wkdir):

	wkdir = os.path.abspath(wkdir)
    md5sumscript_5.create_md5(org_create_list, runfolders)

if __name__ == "__main__":
	main(sys,argv[1], sys.argv[2])
    
