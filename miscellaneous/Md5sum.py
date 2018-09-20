#!usr/bin/python

import datetime
import sys
import os
import subprocess
import glob
import re

class Md5sum(object):
	"""A toolkit for checking md5sums of files"""

	version = "0.1"

	def __init__(self, md5sumvalue):
		self.md5sumvalue =md5sumvalue

	def md5sumvalue(self, filewithoutmd5):
		"""generate a md5sum for a file"""
		filewithoutmd5 = os.path.abspath(filewithoutmd5)
		md5dir = filewithoutmd5.split("/")[:-1]
		md5file = filewithoutmd5 + ".md5"
		createmd5 = "md5sum {} > {}".format(filewithoutmd5, md5file)
            print (createmd5)
            subprocess.call(createmd5, shell=True)
            print ("new md5 file {} generated".format(md5file))
            with open (os.path.join(rf_path, 'new_md5.txt'), 'a') as new_md5:
                new_md5.writelines('new md5 file {} generated'.format(md5file))           

