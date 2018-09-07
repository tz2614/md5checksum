#!usr/bin/python

from __future__ import print_function
import md5sumscript
import pytest
import glob
import string
import os

@pytest.mark.usefixtures("create_runfolder_name","create_sample_name", "create_org_runfolder", "create_bam_in_org", "create_md5_in_org")
class Test_create_two_lists(object):
		
	def test_lists_are_lists(rf_path):
		result1, result2 = md5sumscript.create_two_lists(rf_path)
		assert type(result1) is list, "bam list NOT a list"
		assert type(result2) is list, "md5 list NOT a list"

	def test_list_contain_bam_md5_path(rf_path):
		result1, result2 = md5sumscript.create_two_lists(rf_path)
		assert (bam_path.split(".")[-1] for bam_path in result1) == "bam", "{} path is NOT a bam file".format(bam_path)
		assert ((md5_path.split(".")[-1] for md5_path in result2) and (md5_path.split(".")[-2] for md5_path in result2 == "bam")), "{} path is NOT a bam associated md5 file".format(md5_path)

	def test_list_contain_abspath(create_org_runfolder):
		result1, result2 = md5sumscript.create_two_lists(rf_path)
		assert os.path.isabs(path for path in result1), "{} path is NOT an absolute path"
		assert os.path.isabs(path for path in result2), "{} path is NOT an absolute path"

@pytest.mark.usefixtures("create_runfolder_name","create_sample_name", "create_org_runfolder", "create_bam_in_org", "create_md5_in_org")
class Test_create_logfile(object):

	def test_rf_path_has_write_permission(rf_path):
		assert os.access((rf_path), os.W_OK), "NO write permission for given runfolder path"

	def test_rf_path_has_read_permission(rf_path):
		assert os.access((rf_path), os.R_OK), "NO read permission for given runfolder path"

	def test_rf_path_is_string(rf_path):
		assert type(rf_path) is string, "runfolder path is NOT a string"

	def test_checkfilepath_already_exist(rf_path):
		result = md5sumscript.create_logfile(rf_path)
		assert os.path.exist(result), "checkfile path DO NOT exist"

	def test_checkfilepath_format(rf_path):
		result = md5sumscript.create_logfile(rf_path)
		year = result.split("/")[-1].split("-")[0]
		month = result.split("/")[-1].split("-")[1]
		day = result.split("/")[-1].split("-")[2].split(".")[0]
		filetype = result.split("/")[-1].split("-")[-1].split(".")[-1]
		assert year.isdigit(), "year given NOT a number" 
		assert len(year) == 4, "year NOT 4 digit long" 
		assert month.isdigit(), "month given NOT a number" 
		assert len(month) == 2, "month given NOT 2 digit long" 
		assert day.isdigit(), "day given NOT a number" 
		assert len(day) == 2, "day given NOT 2 digit long" 
		assert filetype == "chk", "file type NOT chk"

@pytest.mark.usefixtures("create_runfolder_name","create_sample_name", "create_org_runfolder", "create_bam_in_org", "create_md5_in_org")
class Test_check_md5_format(md5_sumscript.create_logfile)