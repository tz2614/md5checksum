#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re

"""how to generate a new md5 for any given file"""

def md5sumvalue(filewithoutmd5):
	"""generate a md5sum for a file"""
	filewithoutmd5 = os.path.abspath(filewithoutmd5)
	md5dir = os.path.dirname(filewithoutmd5)
	print (md5dir)
	md5file = filewithoutmd5 + ".md5"
	print (md5file)
	createmd5 = "md5sum {} > {}".format(filewithoutmd5, md5file)
	print (createmd5)
	subprocess.call(createmd5, shell=True)
	print ("new md5 file {} generated".format(md5file))
	with open (os.path.join(md5dir, 'new_md5.txt'), 'a') as new_md5:
		new_md5.writelines('new md5 file {} generated'.format(md5file))     

def main(filewithoutmd5):

	md5sumvalue(filewithoutmd5)

if __name__ == "__main__":
	main((sys.argv[1]))