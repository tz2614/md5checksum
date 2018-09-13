#!usr/bin/python

from __future__ import print_function
import md5sumscript
import pytest
import glob
import string
import os
import shutil

# directories containing test datasets for the md5checksum program
org_rf_path1 = "/mnt/storage/home/zhengt/projects/testrunfolder/original/runfolder1"
org_rf_path2 = "/mnt/storage/home/zhengt/projects/testrunfolder/original/runfolder2"
org_rf_path3 = "/mnt/storage/home/zhengt/projects/testrunfolder/original/runfolder3"
bkup_rf_path1 = "/mnt/storage/home/zhengt/projects/testrunfolder/backup/180725/runfolder1"
bkup_rf_path2 = "/mnt/storage/home/zhengt/projects/testrunfolder/backup/180725/runfolder2"
bkup_rf_path3 = "/mnt/storage/home/zhengt/projects/testrunfolder/backup/180725/runfolder3"

directory1 = "pytest_scenario1" # temp bam and md5 for scenario1
directory2 = "pytest_scenario2" # temp bam and md5 for scenario2
directory3 = "pytest_scenario3" # temp bam and md5 for scenario3
directory4 = "pytest_scenario4" # temp bam and md5 for scenario4
directory5 = "pytest_scenario5" # temp bam and md5 for scenario5
directory6 = "pytest_scenario6" # temp bam and md5 for scenario6
directory7 = "pytest_scenario6" # temp bam and md5 for scenario7
directory8 = "pytest_scenario6" # temp bam and md5 for scenario8
directory9 = "pytest_scenario6" # temp bam and md5 for scenario9

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture")
def test_create_two_lists():

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
	org_rf_path_9, bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_sample_bam_9 = scenario_9_fixture()
	
	org_bam_list_1, org_md5_list_1 = md5sumscript.create_two_lists(org_rf_path_1)
	bkup_bam_list_1, bkup_md5_list_1 = md5sumscript.create_two_lists(bkup_rf_path_1)

	org_bam_list_7, org_md5_list_7 = md5sumscript.create_two_lists(org_rf_path_7)
	bkup_bam_list_7, bkup_md5_list_7 = md5sumscript.create_two_lists(bkup_rf_path_7)

	org_bam_list_8, org_md5_list_8 = md5sumscript.create_two_lists(org_rf_path_8)
	bkup_bam_list_8, bkup_md5_list_8 = md5sumscript.create_two_lists(bkup_rf_path_8)

	org_bam_list_9, org_md5_list_9 = md5sumscript.create_two_lists(org_rf_path_9)
	bkup_bam_list_9, bkup_md5_list_9 = md5sumscript.create_two_lists(bkup_rf_path_9)

	assert (bam_path.split(".")[-1] for bam_path in org_bam_list_1) == "bam", "{} in original is NOT a bam file".format(bam_path)
	assert (bam_path.split(".")[-1] for bam_path in bkup_bam_list_1) == "bam", "{} in backup is NOT a bam file".format(bam_path)
	assert (md5_path.split(".")[-1] for md5_path in org_md5_list_1 == "md5") and (md5_path.split(".")[-2] for md5_path in org_md5_list_1 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)
	assert (md5_path.split(".")[-1] for md5_path in bkup_md5_list_1 == "md5") and (md5_path.split(".")[-2] for md5_path in bkup_md5_list_1 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)

	assert (bam_path.split(".")[-1] for bam_path in org_bam_list_7) == "bam", "{} in original is NOT a bam file".format(bam_path)
	assert (bam_path.split(".")[-1] for bam_path in bkup_bam_list_7) == "bam", "{} in backup is NOT a bam file".format(bam_path)
	assert (md5_path.split(".")[-1] for md5_path in org_md5_list_7 == "md5") and (md5_path.split(".")[-2] for md5_path in org_md5_list_7 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)
	assert (md5_path.split(".")[-1] for md5_path in bkup_md5_list_7 == "md5") and (md5_path.split(".")[-2] for md5_path in bkup_md5_list_7 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)

	assert (bam_path.split(".")[-1] for bam_path in org_bam_list_8) == "bam", "{} in original is NOT a bam file".format(bam_path)
	assert (bam_path.split(".")[-1] for bam_path in bkup_bam_list_8) == "bam", "{} in backup is NOT a bam file".format(bam_path)
	assert (md5_path.split(".")[-1] for md5_path in org_md5_list_8 == "md5") and (md5_path.split(".")[-2] for md5_path in org_md5_list_8 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)
	assert (md5_path.split(".")[-1] for md5_path in bkup_md5_list_8 == "md5") and (md5_path.split(".")[-2] for md5_path in bkup_md5_list_8 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)

	assert (bam_path.split(".")[-1] for bam_path in org_bam_list_9) == "bam", "{} in original is NOT a bam file".format(bam_path)
	assert (bam_path.split(".")[-1] for bam_path in bkup_bam_list_9) == "bam", "{} in backup is NOT a bam file".format(bam_path)
	assert (md5_path.split(".")[-1] for md5_path in org_md5_list_9 == "md5") and (md5_path.split(".")[-2] for md5_path in org_md5_list_9 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)
	assert (md5_path.split(".")[-1] for md5_path in bkup_md5_list_9 == "md5") and (md5_path.split(".")[-2] for md5_path in bkup_md5_list_9 == "bam"), "{} is NOT a bam associated md5 file".format(md5_path)

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture")
class Test_check_md5_exist(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
	org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
	org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
	org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()

	md5_list = [new_org_sample_md5_1, new_org_sample_md5_2, new_org_sample_md5_3, new_org_sample_md5_4, new_org_sample_md5_5, new_org_sample_md5_6, new_org_sample_md5_7, new_bkup_sample_md5_1, new_bkup_sample_md5_2, new_bkup_sample_md5_3, new_bkup_sample_md5_4, new_bkup_sample_md5_5, new_bkup_sample_md5_6, new_bkup_sample_md5_8]

	def test_md5_exist():

		assert md5sumscript.check_md5_exist(new_org_sample_md5_1, md5sumscript.create_md5_missing_logfile(org_rf_path1)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_2, md5sumscript.create_md5_missing_logfile(org_rf_path2)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_3, md5sumscript.create_md5_missing_logfile(org_rf_path3)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_4, md5sumscript.create_md5_missing_logfile(org_rf_path4)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_5, md5sumscript.create_md5_missing_logfile(org_rf_path5)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_6, md5sumscript.create_md5_missing_logfile(org_rf_path6)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_org_sample_md5_7, md5sumscript.create_md5_missing_logfile(org_rf_path7)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_1, md5sumscript.create_md5_missing_logfile(bkup_rf_path1)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_2, md5sumscript.create_md5_missing_logfile(bkup_rf_path2)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_3, md5sumscript.create_md5_missing_logfile(bkup_rf_path3)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_4, md5sumscript.create_md5_missing_logfile(bkup_rf_path4)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_5, md5sumscript.create_md5_missing_logfile(bkup_rf_path5)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_6, md5sumscript.create_md5_missing_logfile(bkup_rf_path6)), "md5 DO NOT exist"
		assert md5sumscript.check_md5_exist(new_bkup_sample_md5_8, md5sumscript.create_md5_missing_logfile(bkup_rf_path8)), "md5 DO NOT exist"

	def test_md5_missing_log(md5_list):

		for md5 in md5_list:
			
			logfile = "".join(md5.split("/")[:-1]) + "md5_missing.txt"

			try:
				f = open (logfile, 'r')
				lines = f.readlines()
				for line in lines:
					if line.startswith("time of check:") 
						print ("time logged")
					elif:
						"present" in line:
						 print (md5 "checked")
					elif:
						"file missing" in line:
						print (md5, "missing status recorded")

			except:
				return None

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture")
class Test_create_md5(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
	org_rf_path_9, bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_sample_bam_9 = scenario_9_fixture()
	
	bam_list_1, md5_list_1 = md5sumscript.create_two_lists(org_rf_path_1)
	bam_list_7, md5_list_7 = md5sumscript.create_two_lists(org_rf_path_7)
	bam_list_8, md5_list_8 = md5sumscript.create_two_lists(org_rf_path_8)
	bam_list_9, md5_list_9 = md5sumscript.create_two_lists(org_rf_path_9)

	new_org_md5_list_1 = md5sumscript.create_md5(bam_list_1, org_rf_path_1)
	new_org_md5_list_7 = md5sumscript.create_md5(bam_list_7, org_rf_path_7)
	new_org_md5_list_8 = md5sumscript.create_md5(bam_list_8, org_rf_path_8)
	new_org_md5_list_9 = md5sumscript.create_md5(bam_list_9, org_rf_path_9)

	new_bkup_md5_list_1 = md5sumscript.create_md5(bam_list_1, bkup_rf_path_1)
	new_bkup_md5_list_7 = md5sumscript.create_md5(bam_list_7, bkup_rf_path_7)
	new_bkup_md5_list_8 = md5sumscript.create_md5(bam_list_8, bkup_rf_path_8)
	new_bkup_md5_list_9 = md5sumscript.create_md5(bam_list_9, bkup_rf_path_9)

	new_md5_lists = [new_md5_list_1, new_md5_list_7, new_md5_list_8, new_md5_list_9, new_bkup_md5_list_1, new_bkup_md5_list_7, new_bkup_md5_list_8, new_bkup_md5_list_9]

	def test_if_new_md5s_exist(new_md5_lists):

		new_md5s = []

		for md5_list in new_md5_lists:

			for md5 in md5_list:

				if os.path.exists(md5):
					print ("{} generated".format(md5))
					continue
				else:
					new_md5s.append(md5)
					print ("md5 do not exist")

			assert md5_list == new_md5s, "list of new md5s generated incorrect"

	def test_md5_missing_log_format(new_md5_lists):

		for md5_list in new_md5_lists

			for md5 in new_md5_list:

				logfile = "".join(md5.split("/")[:-1]) + "md5_missing.txt"

				f = open (logfile, 'r')
				
				lines = f.readlines()

				for line in lines:
					if line.startswith("time of generation:"):
						print ("time of md5 generation logged")
					elif:
						line.startswith("new md5 file") and md5 in line:
						print ("new md5 file recorded correctly in log")
					else:
						print ("wrong md5 file recorded in log")
						continue

				f.close()

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture")
class Test_create_logfile(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
	org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
	org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
	org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()

	rf_path_list = [org_rf_path_1, org_rf_path_2, org_rf_path_3, org_rf_path_4, org_rf_path_5, org_rf_path_6, org_rf_path_7, org_rf_path_8, bkup_rf_path_1, bkup_rf_path_2, bkup_rf_path_3, bkup_rf_path_4, bkup_rf_path_5, bkup_rf_path_6, bkup_rf_path_7, bkup_rf_path_8]
	
	def test_rf_path_has_write_permission(rf_path_list):

		for rf_path in rf_path_list:
			assert os.access((rf_path), os.W_OK), "NO write permission for {}".format(rf_path)
	
	def test_rf_path_has_read_permission(rf_path):
		
		for rf_path in rf_path_list:
			assert os.access((rf_path), os.R_OK), "NO read permission for {}".format(rf_path)
	
	def test_rf_path_is_string(rf_path_list):

		for rf_path in rf_path_list:
			assert type(rf_path) is str, "runfolder path is NOT a string"

	def test_checkfilepath(rf_path_list):

		for rf_path in rf_path_list:		
			checkfilepath = md5sumscript.create_logfile(rf_path)

			assert os.path.exists(checkfilepath), "{} DO NOT exist".format(checkfilepath)

			year = checkfilepath.split("/")[-1].split("-")[0]
			month = checkfilepath.split("/")[-1].split("-")[1]
			day = checkfilepath.split("/")[-1].split("-")[2].split(".")[0]
			filetype = checkfilepath.split("/")[-1].split("-")[-1].split(".")[-1]
			assert year.isdigit(), "year given NOT a number" 
			assert len(year) == 4, "year NOT 4 digit long" 
			assert month.isdigit(), "month given NOT a number" 
			assert len(month) == 2, "month given NOT 2 digit long" 
			assert day.isdigit(), "day given NOT a number" 
			assert len(day) == 2, "day given NOT 2 digit long" 
			assert filetype == "chk", "file type NOT chk"	

@pytest.mark.usefixtures("scenario_3_fixture")
class Test_check_md5_hash(object):

	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()

	org_checkfilepath_3 = md5sumscript.create_logfile(org_rf_path3)
	bkup_checkfilepath_3 = md5sumscript.create_logfile(bkup_rf_path3)

	with open (new_org_sample_md5_3, "r") as md5_file:
		org_checksum_3 = md5_file.readline().strip()[:32]
	with open (new_bkup_sample_md5_3, "r") as md5_file:
		bkup_checksum_3 = md5_file.readline().strip()[:32]
		
	org_hash_check_3 = md5sumscript.check_md5_hash(org_checkfilepath_3, new_org_sample_md5_3, org_checksum_3)
	bkup_hash_check_3 = md5sumscript.check_md5_hash(bkup_checkfilepath_3, new_bkup_sample_md5_3, bkup_checksum_3)
	
	def test_check_hash_format():

		# check the md5 hash has correct format
		
			org_chars_3 = ""
			bkup_chars_3 = ""

			try:
				for char in org_checksum_3:
					if char in string.ascii_letters() or char in string.digits():
						org_chars_3 += char

				for char in bkup_checksum_3:
					if char in string.ascii_letters() or char in string.digits():
						bkup_chars_3 += char

			except:
				print ("characters in checksum NOT in correct format")
				return None

		assert org_chars_3 == org_checksum_3, "check_md5_hash function NOT working for {}".format(new_org_sample_md5_3)
		assert bkup_chars_3 == bkup_checksum_3, "check_md5_hash function NOT working for {}".format(new_bkup_sample_md5_3)
		

	def test_check_hash_length():

		# check the md5 hash in the md5 file has correct length
		count = 0
		for char in org_checksum_3:
			count += 1

		org_len_3 = count

		count = 0
		for char in bkup_checksum_3:
			count += 1

		bkup_len_3 = count

		assert org_len_3 == 32, "length of md5 hash incorrect for {}".format(new_org_sample_md5_3)
		assert bkup_len_3 == 32, "length of md5 hash incorrect for {}".format(new_bkup_sample_md5_3)

	
	def test_logfile_content():

		checkfilepaths = [org_checkfilepath_3, bkup_checkfilepath_3]

		for checkfilepath in checkfilepaths:

			with open (checkfilepath, "r") as checkfile:
				for line in checkfile:
					if "OK" and "have 32 characters and contain only letters or numbers" in line:
						print ("correct format recorded")
					elif "time of hash check:" in line:
						print ("hash check time logged")
					elif "ERROR" and "DO NOT have 32 characters or contain non-alphanumeric characters" in line:
						print ("correct format recorded")
					else:
						continue

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_4_fixture")
class Test_check_filename_match(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
	org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
	org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
	org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
	
	org_checkfilepath_1 = md5sumscript.create_logfile(org_rf_path_1)
	bkup_checkfilepath_1 = md5sumscript.create_logfile(bkup_rf_path_1)

	org_checkfilepath_2 = md5sumscript.create_logfile(org_rf_path_2)
	bkup_checkfilepath_2 = md5sumscript.create_logfile(bkup_rf_path_2)

	org_checkfilepath_3 = md5sumscript.create_logfile(org_rf_path_3)
	bkup_checkfilepath_3 = md5sumscript.create_logfile(bkup_rf_path_3)

	org_checkfilepath_4 = md5sumscript.create_logfile(org_rf_path_4)
	bkup_checkfilepath_4 = md5sumscript.create_logfile(bkup_rf_path_4)

	org_checkfilepath_5 = md5sumscript.create_logfile(org_rf_path_5)
	bkup_checkfilepath_5 = md5sumscript.create_logfile(bkup_rf_path_5)

	org_checkfilepath_6 = md5sumscript.create_logfile(org_rf_path_6)
	bkup_checkfilepath_6 = md5sumscript.create_logfile(bkup_rf_path_6)

	org_checkfilepath_7 = md5sumscript.create_logfile(org_rf_path_7)
	bkup_checkfilepath_7 = md5sumscript.create_logfile(bkup_rf_path_7)

	org_checkfilepath_8 = md5sumscript.create_logfile(org_rf_path_8)
	bkup_checkfilepath_8 = md5sumscript.create_logfile(bkup_rf_path_8)

	checkfilepaths = [org_checkfilepath_1, bkup_checkfilepath_1, org_checkfilepath_2, bkup_checkfilepath_2, org_checkfilepath_3, bkup_checkfilepath_3, org_checkfilepath_4, bkup_checkfilepath_4, org_checkfilepath_5, bkup_checkfilepath_5, org_checkfilepath_6, bkup_checkfilepath_6, org_checkfilepath_7, bkup_checkfilepath_8]

	org_bam_filename_1 = new_org_sample_bam_1.split("/")[-1]
	bkup_bam_filename_1 = new_bkup_sample_bam_1.split("/")[-1]
	org_bam_filename_2 = new_org_sample_bam_2.split("/")[-1]
	bkup_bam_filename_2 = new_bkup_sample_bam_2.split("/")[-1]
	org_bam_filename_3 = new_org_sample_bam_3.split("/")[-1]
	bkup_bam_filename_3 = new_bkup_sample_bam_3.split("/")[-1]
	org_bam_filename_4 = new_org_sample_bam_4.split("/")[-1]
	bkup_bam_filename_4 = new_bkup_sample_bam_4.split("/")[-1]
	org_bam_filename_5 = new_org_sample_bam_5.split("/")[-1]
	bkup_bam_filename_5 = new_bkup_sample_bam_5.split("/")[-1]
	org_bam_filename_6 = new_org_sample_bam_6.split("/")[-1]
	bkup_bam_filename_6 = new_bkup_sample_bam_6.split("/")[-1]
	org_bam_filename_7 = new_org_sample_bam_7.split("/")[-1]
	org_bam_filename_8 = new_org_sample_bam_8.split("/")[-1]
	bkup_bam_filename_8 = new_bkup_sample_bam_8.split("/")[-1]

	with open (new_org_sample_md5_1, "r") as md5_file:
		org_bam_1 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_1, "r") as md5_file:
		bkup_bam_1 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_2, "r") as md5_file:
		org_bam_2 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_2, "r") as md5_file:
		bkup_bam_2 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_3, "r") as md5_file:
		org_bam_3 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_3, "r") as md5_file:
		bkup_bam_3 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_4, "r") as md5_file:
		org_bam_4 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_4, "r") as md5_file:
		bkup_bam_4 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_5, "r") as md5_file:
		org_bam_5 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_5, "r") as md5_file:
		bkup_bam_5 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_6, "r") as md5_file:
		org_bam_6 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_6, "r") as md5_file:
		bkup_bam_6 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_7, "r") as md5_file:
		org_bam_7 = md5_file.readline().strip().split("  ")[-1]
	with open (new_org_sample_md5_8, "r") as md5_file:
		org_bam_8 = md5_file.readline().strip().split("  ")[-1]
	with open (new_bkup_sample_md5_8, "r") as md5_file:
		bkup_bam_8 = md5_file.readline().strip().split("  ")[-1]

	def test_filename_match():
		
		assert check_filename_match(org_checkfilepath_1, org_md5_filename_1, org_bam_1, new_org_sample_md5_1), "check_filename_match function NOT working"
		assert check_filename_match(bkup_checkfilepath_1, bkup_md5_filename_1, bkup_bam_1, new_bkup_sample_md5_1), "check_filename_match function NOT working"
		assert check_filename_match(org_checkfilepath_3, org_md5_filename_3, org_bam_3, new_org_sample_md5_3), "check_filename_match function NOT working"
		assert check_filename_match(bkup_checkfilepath_3, bkup_md5_filename_3, bkup_bam_3, new_bkup_sample_md5_3), "check_filename_match function NOT working"
		assert check_filename_match(org_checkfilepath_7, org_md5_filename_7, org_bam_7, new_org_sample_md5_7), "check_filename_match function NOT working"
		assert check_filename_match(org_checkfilepath_8, org_md5_filename_8, org_bam_8, new_org_sample_md5_8), "check_filename_match function NOT working"
		assert check_filename_match(bkup_checkfilepath_8, bkup_md5_filename_8, bkup_bam_8, new_bkup_sample_md5_8), "check_filename_match function NOT working"

	def test_filename_mismatch():

		assert not check_filename_match(org_checkfilepath_2, org_md5_filename_2, org_bam_2, new_org_sample_md5_2), "check_filename_match function NOT working"
		assert not check_filename_match(bkup_checkfilepath_2, bkup_md5_filename_2, bkup_bam_2, new_bkup_sample_md5_2), "check_filename_match function NOT working"
		assert not check_filename_match(org_checkfilepath_4, org_md5_filename_4, org_bam_4, new_org_sample_md5_4), "check_filename_match function NOT working"
		assert not check_filename_match(bkup_checkfilepath_4, bkup_md5_filename_4, bkup_bam_4, new_bkup_sample_md5_4), "check_filename_match function NOT working"
		assert not check_filename_match(org_checkfilepath_5, org_md5_filename_5, org_bam_5, new_org_sample_md5_5), "check_filename_match function NOT working"
		assert not check_filename_match(bkup_checkfilepath_5, bkup_md5_filename_5, bkup_bam_5, new_bkup_sample_md5_5), "check_filename_match function NOT working"
		assert not check_filename_match(org_checkfilepath_6, org_md5_filename_6, org_bam_6, new_org_sample_md5_6), "check_filename_match function NOT working"
		assert not check_filename_match(bkup_checkfilepath_2, bkup_md5_filename_6, bkup_bam_6, new_bkup_sample_md5_6), "check_filename_match function NOT working"

	def test_logfile_content():

		for checkfilepath in checkfilepaths:

			with open (checkfilepath, "r") as checkfile:
				for line in checkfile:

					if line.startswith(new_org_sample_md5_1) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_1))

					elif line.startswith(new_org_sample_md5_2) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_2))

					elif line.startswith(new_org_sample_md5_3) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_3))

					elif line.startswith(new_org_sample_md5_4) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_4))

					elif line.startswith(new_org_sample_md5_5) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_5))

					elif line.startswith(new_org_sample_md5_6) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_6))

					elif line.startswith(new_org_sample_md5_7) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_7))

					elif line.startswith(new_org_sample_md5_8) and "file is being checked" in line:
						print ("{} file has been checked".format(new_org_sample_md5_8))

					elif line.startswith(new_bkup_sample_md5_1) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_1))

					elif line.startswith(new_bkup_sample_md5_2) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_2))

					elif line.startswith(new_bkup_sample_md5_3) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_3))

					elif line.startswith(new_bkup_sample_md5_4) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_4))

					elif line.startswith(new_bkup_sample_md5_5) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_5))

					elif line.startswith(new_bkup_sample_md5_6) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_6))

					elif line.startswith(new_bkup_sample_md5_7) and "file is being checked" in line:
						print ("{} file has been checked".format(new_bkup_sample_md5_7))

					elif "OK" and "match" and "in" in line:
						print ("correct format recorded")
					elif "time of filename check:" in line:
						print ("filename check time logged")
					elif "ERROR" and "DO NOT match" and "in" in line:
						print ("correct format recorded")
					else:
						continue

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture")
class Test_check_md5(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
	org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
	org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
	org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()

	md5_list = [new_org_sample_md5_1, new_org_sample_md5_2, new_org_sample_md5_3, new_org_sample_md5_4, new_org_sample_md5_5, new_org_sample_md5_6, new_org_sample_md5_7, new_bkup_sample_md5_1, new_bkup_sample_md5_2, new_bkup_sample_md5_3, new_bkup_sample_md5_4, new_bkup_sample_md5_5, new_bkup_sample_md5_6, new_bkup_sample_md5_8]

	org_checkfilepath_1 = md5sumscript.create_logfile(org_rf_path_1)
	bkup_checkfilepath_1 = md5sumscript.create_logfile(bkup_rf_path_1)

	org_checkfilepath_2 = md5sumscript.create_logfile(org_rf_path_2)
	bkup_checkfilepath_2 = md5sumscript.create_logfile(bkup_rf_path_2)

	org_checkfilepath_3 = md5sumscript.create_logfile(org_rf_path_3)
	bkup_checkfilepath_3 = md5sumscript.create_logfile(bkup_rf_path_3)

	org_checkfilepath_4 = md5sumscript.create_logfile(org_rf_path_4)
	bkup_checkfilepath_4 = md5sumscript.create_logfile(bkup_rf_path_4)

	org_checkfilepath_5 = md5sumscript.create_logfile(org_rf_path_5)
	bkup_checkfilepath_5 = md5sumscript.create_logfile(bkup_rf_path_5)

	org_checkfilepath_6 = md5sumscript.create_logfile(org_rf_path_6)
	bkup_checkfilepath_6 = md5sumscript.create_logfile(bkup_rf_path_6)

	org_checkfilepath_7 = md5sumscript.create_logfile(org_rf_path_7)
	bkup_checkfilepath_7 = md5sumscript.create_logfile(bkup_rf_path_7)

	org_checkfilepath_8 = md5sumscript.create_logfile(org_rf_path_8)
	bkup_checkfilepath_8 = md5sumscript.create_logfile(bkup_rf_path_8)

	checkfilepaths = [org_checkfilepath_1, bkup_checkfilepath_1, org_checkfilepath_2, bkup_checkfilepath_2, org_checkfilepath_3, bkup_checkfilepath_3, org_checkfilepath_4, bkup_checkfilepath_4, org_checkfilepath_5, bkup_checkfilepath_5, org_checkfilepath_6, bkup_checkfilepath_6, org_checkfilepath_7, bkup_checkfilepath_8]

	org_bam_list_1, org_md5_list_1 = md5sumscript.create_two_lists(org_rf_path_1)
	bkup_bam_list_1, bkup_md5_list_1 = md5sumscript.create_two_lists(bkup_rf_path_1)

	org_bam_list_2, org_md5_list_2 = md5sumscript.create_two_lists(org_rf_path_2)
	bkup_bam_list_2, bkup_md5_list_2 = md5sumscript.create_two_lists(bkup_rf_path_2)

	org_bam_list_3, org_md5_list_3 = md5sumscript.create_two_lists(org_rf_path_3)
	bkup_bam_list_3, bkup_md5_list_3 = md5sumscript.create_two_lists(bkup_rf_path_3)

	org_bam_list_4, org_md5_list_4 = md5sumscript.create_two_lists(org_rf_path_4)
	bkup_bam_list_4, bkup_md5_list_4 = md5sumscript.create_two_lists(bkup_rf_path_4)

	org_bam_list_5, org_md5_list_5 = md5sumscript.create_two_lists(org_rf_path_5)
	bkup_bam_list_5, bkup_md5_list_5 = md5sumscript.create_two_lists(bkup_rf_path_5)

	org_bam_list_6, org_md5_list_6 = md5sumscript.create_two_lists(org_rf_path_6)
	bkup_bam_list_6, bkup_md5_list_6 = md5sumscript.create_two_lists(bkup_rf_path_6)

	org_bam_list_7, org_md5_list_7 = md5sumscript.create_two_lists(org_rf_path_7)

	org_bam_list_8, org_md5_list_8 = md5sumscript.create_two_lists(org_rf_path_8)
	bkup_bam_list_8, bkup_md5_list_8 = md5sumscript.create_two_lists(bkup_rf_path_8)

	org_check_dict_1 = check_md5(org_checkfilepath_1, org_md5_list_1)
	bkup_check_dict_1 = check_md5(bkup_checkfilepath_1, bkup_md5_list_1)

	org_check_dict_2 = check_md5(org_checkfilepath_2, org_md5_list_2)
	bkup_check_dict_2 = check_md5(bkup_checkfilepath_2, bkup_md5_list_2)

	org_check_dict_3 = check_md5(org_checkfilepath_3, org_md5_list_3)
	bkup_check_dict_3 = check_md5(bkup_checkfilepath_3, bkup_md5_list_3)	

	org_check_dict_4 = check_md5(org_checkfilepath_4, org_md5_list_4)
	bkup_check_dict_4 = check_md5(bkup_checkfilepath_4, bkup_md5_list_4)

	org_check_dict_5 = check_md5(org_checkfilepath_5, org_md5_list_5)
	bkup_check_dict_5 = check_md5(bkup_checkfilepath_5, bkup_md5_list_5)

	org_check_dict_6 = check_md5(org_checkfilepath_6, org_md5_list_6)
	bkup_check_dict_6 = check_md5(bkup_checkfilepath_6, bkup_md5_list_6)

	org_check_dict_7 = check_md5(org_checkfilepath_7, org_md5_list_7)

	org_check_dict_8 = check_md5(org_checkfilepath_8, org_md5_list_8)
	bkup_check_dict_8 = check_md5(bkup_checkfilepath_8, bkup_md5_list_8)

	def test_check_dict():

		org_bkup_dict_1 = {"sample1.bam.md5" : "8620b0a9852e248c88b3f7ed30e73d01"}
		org_bkup_dict_2 = {"sample2.bam.md5" : "0cc1f1cc52cc2d0ed218337cf947eeb8"}				
		org_dict_3 = {"sample3.bam.md5" : "a5119b252ab16786e583b550fab714ac"}
		bkup_dict_3 = {"sample3.bam.md5" : "a5119b252ab16786e583b550fab714ad"}

		org_bkup_dict_4 = {"sample1.bam.md5" : "15f1891487fd6b26f752b50468adb49f"}
		org_bkup_dict_5 = {"sample2.bam.md5" : "15f1891487fd6b26f752b50468adb49f"}
		org_bkup_dict_6 = {"sample3.bam.md5" : "15f1891487fd6b26f752b50468adb59f"}

		org_dict_7 = {"sample1.bam.md5" : "fa0aaaeaf163a93c9e4b96d757079032"}

		org_bkup_dict_8 = {"sample1.bam.md5" : "38f7c7e572fe7aeffe4fcf5728c31f5d"}
		
		assert org_check_dict_1.items() in org_bkup_dict_1.items(), "md5 filename and hash not present in org case 1"
		assert bkup_check_dict_1.items() in org_bkup_dict_1.items(), "md5 filename and hash not present in bkup case 1"
		assert org_check_dict_2.items() in org_bkup_dict_2.items(), "md5 filename and hash not present in org case 2"
		assert bkup_check_dict_2.items() in org_bkup_dict_2.items(), "md5 filename and hash not present in bkup case 2"
		assert org_check_dict_3.items() in org_dict_3.items(), "md5 filename and hash not present in org case 3"
		assert bkup_check_dict_3.items() in bkup_dict_3.items(), "md5 filename and hash not present in bkup case 3"
		assert org_check_dict_4.items() in org_bkup_dict_4.items(), "md5 filename and hash not present in org case 4"
		assert bkup_check_dict_4.items() in org_bkup_dict_4.items(), "md5 filename and hash not present in bkup case 4"
		assert org_check_dict_5.items() in org_bkup_dict_5.items(), "md5 filename and hash not present in org case 5"
		assert bkup_check_dict_5.items() in org_bkup_dict_5.items(), "md5 filename and hash not present in bkup case 5"
		assert org_check_dict_6.items() in org_bkup_dict_6.items(), "md5 filename and hash not present in org case 6"
		assert bkup_check_dict_6.items() in org_bkup_dict_6.items(), "md5 filename and hash not present in bkup case 6"
		assert org_check_dict_7.items() in org_dict_7.items(), "md5 filename and hash not present for case 7"
		assert org_check_dict_8.items() in org_bkup_dict_8.items(), "md5 filename and hash not present for case 7"
		assert bkup_check_dict_8.items() in org_bkup_dict_8.items(), "md5 filename and hash not present for case 8"

	def test_check_file_output():

		org_bam_filename_1 = new_org_sample_bam_1.split("/")[-1]
		bkup_bam_filename_1 = new_bkup_sample_bam_1.split("/")[-1]
		org_bam_filename_2 = new_org_sample_bam_2.split("/")[-1]
		bkup_bam_filename_2 = new_bkup_sample_bam_2.split("/")[-1]
		org_bam_filename_3 = new_org_sample_bam_3.split("/")[-1]
		bkup_bam_filename_3 = new_bkup_sample_bam_3.split("/")[-1]
		org_bam_filename_4 = new_org_sample_bam_4.split("/")[-1]
		bkup_bam_filename_4 = new_bkup_sample_bam_4.split("/")[-1]
		org_bam_filename_5 = new_org_sample_bam_5.split("/")[-1]
		bkup_bam_filename_5 = new_bkup_sample_bam_5.split("/")[-1]
		org_bam_filename_6 = new_org_sample_bam_6.split("/")[-1]
		bkup_bam_filename_6 = new_bkup_sample_bam_6.split("/")[-1]
		org_bam_filename_7 = new_org_sample_bam_7.split("/")[-1]
		org_bam_filename_8 = new_org_sample_bam_8.split("/")[-1]
		bkup_bam_filename_8 = new_bkup_sample_bam_8.split("/")[-1]

		for checkfilepath in checkfilepaths:

			with open(checkfilepath, "r") as checkfile:

				for line in checkfile.readlines():

					elif line.startswith("md5sum:") and "WARNING:" in line and "1 listed file could not be read" in line:
						print ("md5sum -c program executed correctly, with WARNING message stating file CANNOT BE READ")

					elif line.startswith("md5sum:") and "WARNING:" in line and "1 computed checksum did NOT match" in line:
						print ("md5sum -c program executed correctly, with WARNING message stating file checksum DO NOT match")

					elif line.startswith(org_bam_filename_1) and "OK" in line:
						print ("{} recorded in log file, and hash match".format(org_bam_filename_1))

					elif line.startswith("sample1.bam") and "FAILED" in line:
						print ("{} recorded in log file, and hash DO NOT match".format("sample1.bam"))

					elif line.startswith("md5sum:") and ("sample22.bam") in line and "No such file or directory" in line:
						print ("md5sum -c program executed for {}, bam file stated does NOT exist".format("sample22.bam"))

					elif line.startswith("sample22.bam") and "FAILED open or read" in line:
						print ("md5sum -c program executed for {}, bam file cannot be opened or read".format("sample22.bam"))

					elif line.startswith("sample3.bam") and "FAILED" in line:
						print ("{} recorded in log file, and hash DO NOT match".format("sample3.bam"))

					elif line.startswith("sample1.bam") and "FAILED" in line:
						print ("{} recorded in log file, and hash DO NOT match".format("sample1.bam"))

					elif line.startswith("md5sum:") and (org_bam_filename_4) in line and "No such file or directory" in line:
						print ("md5sum -c program executed for {}, bam file stated does NOT exist". format(org_bam_filename_4))

					elif line.startswith(org_bam_filename_4) and "FAILED open or read" in line:
						print ("md5sum -c program executed for {}, bam file cannot be opened or read". format(org_bam_filename_4))

					elif line.startswith("md5sum:") and ("runfolder1/sample1.bam") in line and "No such file or directory" in line:
						print ("md5sum -c program executed for {}, bam file stated does NOT exist". format("runfolder1/sample1.bam"))

					elif line.startswith("runfolder1/sample1.bam") and "FAILED open or read" in line:
						print ("md5sum -c program executed for {}, bam file cannot be opened or read". format("runfolder1/sample1.bam"))

					elif line.startswith(org_bam_filename_7) and "OK" in line:
						print ("{} recorded in log file, and hash match".format(org_bam_filename_7))

					elif line.startswith("sample12.bam") and "OK" in line:
						print ("{} recorded in log file, and hash match".format("sample12.bam"))

					elif line.startswith(bkup_bam_filename_7) and "OK" in line:
						print ("{} recorded in log file, and hash match".format(org_bam_filename_1))


@pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture")
class check_org_bkup(object):

	org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
	org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
	org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
	org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
	org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
	org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
	org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
	org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
	org_rf_path_9, bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_sample_bam_9 = scenario_9_fixture()

	org_bam_list_1, org_md5_list_1 = md5sumscript.create_two_lists(org_rf_path_1)
	bkup_bam_list_1, bkup_md5_list_1 = md5sumscript.create_two_lists(bkup_rf_path_1)

	org_bam_list_2, org_md5_list_2 = md5sumscript.create_two_lists(org_rf_path_2)
	bkup_bam_list_2, bkup_md5_list_2 = md5sumscript.create_two_lists(bkup_rf_path_2)

	org_bam_list_3, org_md5_list_3 = md5sumscript.create_two_lists(org_rf_path_3)
	bkup_bam_list_3, bkup_md5_list_3 = md5sumscript.create_two_lists(bkup_rf_path_3)

	org_bam_list_4, org_md5_list_4 = md5sumscript.create_two_lists(org_rf_path_4)
	bkup_bam_list_4, bkup_md5_list_4 = md5sumscript.create_two_lists(bkup_rf_path_4)

	org_bam_list_5, org_md5_list_5 = md5sumscript.create_two_lists(org_rf_path_5)
	bkup_bam_list_5, bkup_md5_list_5 = md5sumscript.create_two_lists(bkup_rf_path_5)

	org_bam_list_6, org_md5_list_6 = md5sumscript.create_two_lists(org_rf_path_6)
	bkup_bam_list_6, bkup_md5_list_6 = md5sumscript.create_two_lists(bkup_rf_path_6)

	org_bam_list_7, org_md5_list_7 = md5sumscript.create_two_lists(org_rf_path_7)
	bkup_bam_list_7, bkup_md5_list_7 = md5sumscript.create_two_lists(bkup_rf_path_7)

	org_bam_list_8, org_md5_list_8 = md5sumscript.create_two_lists(org_rf_path_8)
	bkup_bam_list_8, bkup_md5_list_8 = md5sumscript.create_two_lists(bkup_rf_path_8)

	org_bam_list_9, org_md5_list_9 = md5sumscript.create_two_lists(org_rf_path_9)
	bkup_bam_list_9, bkup_md5_list_9 = md5sumscript.create_two_lists(bkup_rf_path_9)

	new_org_md5_list_7 = md5sumscript.create_md5(org_bam_list_7, org_rf_path_7)
	new_org_md5_list_8 = md5sumscript.create_md5(org_bam_list_8, org_rf_path_8)
	new_org_md5_list_9 = md5sumscript.create_md5(org_bam_list_9, org_rf_path_9)
	new_bkup_md5_list_7 = md5sumscript.create_md5(bkup_bam_list_7, bkup_rf_path_7)
	new_bkup_md5_list_8 = md5sumscript.create_md5(bkup_bam_list_8, bkup_rf_path_8)
	new_bkup_md5_list_9 = md5sumscript.create_md5(bkup_bam_list_9, bkup_rf_path_9)

	md5_lists = [new_org_sample_md5_1, new_org_sample_md5_2, new_org_sample_md5_3, new_org_sample_md5_4, new_org_sample_md5_5, new_org_sample_md5_6, new_org_sample_md5_7, new_bkup_sample_md5_1, new_bkup_sample_md5_2, new_bkup_sample_md5_3, new_bkup_sample_md5_4, new_bkup_sample_md5_5, new_bkup_sample_md5_6, new_bkup_sample_md5_8]
	
	check_dict_1 = md5sumscript.create_check_dict(org_rf_path_1, bkup_rf_path1, org_md5_list_1, bkup_md5_list_1, new_org_md5_list_1, new_bkup_md5_list_1)
	check_dict_2 = md5sumscript.create_check_dict(org_rf_path_2, bkup_rf_path2, org_md5_list_2, bkup_md5_list_2, new_org_md5_list_2, new_bkup_md5_list_2)
	check_dict_3 = md5sumscript.create_check_dict(org_rf_path_3, bkup_rf_path3, org_md5_list_3, bkup_md5_list_3, new_org_md5_list_3, new_bkup_md5_list_3)
	check_dict_4 = md5sumscript.create_check_dict(org_rf_path_4, bkup_rf_path4, org_md5_list_4, bkup_md5_list_4, new_org_md5_list_4, new_bkup_md5_list_4)
	check_dict_5 = md5sumscript.create_check_dict(org_rf_path_5, bkup_rf_path5, org_md5_list_5, bkup_md5_list_5, new_org_md5_list_5, new_bkup_md5_list_5)
	check_dict_6 = md5sumscript.create_check_dict(org_rf_path_6, bkup_rf_path6, org_md5_list_6, bkup_md5_list_6, new_org_md5_list_6, new_bkup_md5_list_6)
	check_dict_7 = md5sumscript.create_check_dict(org_rf_path_7, bkup_rf_path7, org_md5_list_7, bkup_md5_list_7, new_org_md5_list_7, new_bkup_md5_list_7)
	check_dict_8 = md5sumscript.create_check_dict(org_rf_path_8, bkup_rf_path8, org_md5_list_8, bkup_md5_list_8, new_org_md5_list_8, new_bkup_md5_list_8)
	check_dict_9 = md5sumscript.create_check_dict(org_rf_path_9, bkup_rf_path9, org_md5_list_9, bkup_md5_list_9, new_org_md5_list_9, new_bkup_md5_list_9)

	def test_check_md5filename():

		for md5 in org_md5_list_1:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_1, md5_filename, check_dict_1["storage"]), "md5 NOT in original runfolder"

		for md5 in bkup_md5_list_1:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_1, md5_filename, check_dict_1["archive"]), "md5 NOT in backup runfolder"

		for md5 in org_md5_list_2:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_2, md5_filename, check_dict_2["storage"]), "md5 NOT in original runfolder"

		for md5 in bkup_md5_list_2:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_2, md5_filename, check_dict_2["archive"]), "md5 NOT in backup runfolder"

		for md5 in org_md5_list_3:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_3, md5_filename, check_dict_3["storage"]), "md5 NOT in original runfolder"

		for md5 in bkup_md5_list_3:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_3, md5_filename, check_dict_3["archive"]), "md5 NOT in backup runfolder"

		for md5 in org_md5_list_4:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_4, md5_filename, check_dict_4["storage"]), "md5 NOT in original runfolder"

		for md5 in bkup_md5_list_4:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_4, md5_filename, check_dict_4["archive"]), "md5 NOT in backup runfolder"

		for md5 in org_md5_list_5:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_5, md5_filename, check_dict_5["storage"]), "md5 NOT in original runfolder"

		for md5 in bkup_md5_list_5:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_5, md5_filename, check_dict_5["archive"]), "md5 NOT in backup runfolder"

		for md5 in org_md5_list_6:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_6, md5_filename, check_dict_6["storage"]), "md5 NOT in backup runfolder"
		
		for md5 in bkup_md5_list_6:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_6, md5_filename, check_dict_6["archive"]), "md5 NOT in backup runfolder"
		
		for md5 in org_md5_list_7:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_7, md5_filename, check_dict_7["storage"]), "md5 NOT in backup runfolder"
		
		for md5 in bkup_md5_list_7:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_7, md5_filename, check_dict_7["archive"]), "md5 NOT in backup runfolder"
		
		for md5 in org_md5_list_8:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_8, md5_filename, check_dict_8["storage"]), "md5 NOT in backup runfolder"
		
		for md5 in bkup_md5_list_8:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_8, md5_filename, check_dict_8["archive"]), "md5 NOT in backup runfolder"
		
		for md5 in org_md5_list_9:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(org_rf_path_9, md5_filename, check_dict_9["storage"]), "md5 NOT in backup runfolder"

		for md5 in bkup_md5_list_9:
			md5_filename = md5.split("/")[-1]
			assert md5_filename in md5sumscript.check_md5filename(bkup_rf_path_9, md5_filename, check_dict_9["archive"]), "md5 NOT in backup runfolder"

	def test_compare_md5hash():


		for md5 in org_md5_list_1:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_1, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_1, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_1:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_1, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_1, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in org_md5_list_2:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_2, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_2, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_2:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_2, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_2, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in org_md5_list_3:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_3, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_3, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_3:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_3, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_3, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in org_md5_list_4:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_4, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_4, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_4:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_4, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_4, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in org_md5_list_5:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_5, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_5, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_5:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_5, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_5, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in org_md5_list_6:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_6, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_6, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in bkup_md5_list_6:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_6, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_6, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in org_md5_list_7:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_7, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_7, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in bkup_md5_list_7:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_7, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_7, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in org_md5_list_8:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_8, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_8, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in bkup_md5_list_8:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_8, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_8, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
		
		for md5 in org_md5_list_9:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(org_rf_path_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(org_rf_path_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

		for md5 in bkup_md5_list_9:
			md5_filename = md5.split("/")[-1]
			if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
				assert md5sumscript.compare_md5hash(bkup_rf_path_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
			else:
				assert not md5sumscript.compare_md5hash(bkup_rf_path_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	def test_check_hash_exist():

		for md5 in org_md5_list_1:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_1, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_1, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_1, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_1, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_1:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_1, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_1, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_1, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_1, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
		
		for md5 in org_md5_list_2:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_2, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_2, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_2, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_2, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
		
		for md5 in bkup_md5_list_2:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_2, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_2, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_2, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_2, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
		
		for md5 in org_md5_list_3:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_3, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_3, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_3, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_3, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
		
		for md5 in bkup_md5_list_3:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_3, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_3, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_3, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_3, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_4:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_4, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_4, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_4, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_4, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_4:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_4, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_4, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_4, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"				
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_4, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_5:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_5, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_5, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_5, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_5, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_5:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_5, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_5, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_5, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_5, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_6:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_6, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_6, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_6, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_6, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
		
		for md5 in bkup_md5_list_6:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_6, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_6, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_6, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_6, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_7:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_7, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_7, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_7, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_7, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_7:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_7, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_7, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_7, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_7, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_8:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_8, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_8, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_8, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_8, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_8:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_8, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_8, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_8, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_8, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in org_md5_list_9:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(org_rf_path_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(org_rf_path_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

		for md5 in bkup_md5_list_9:
			md5_filename = md5.split("/")[-1]

			if check_dict["archive"][md5_filename] in check_dict["storage"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

			if check_dict["storage"][md5_filename] in check_dict["archive"].values():
				assert md5sumscript.check_hash_exist(bkup_rf_path_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
			else:
				assert not md5sumscript.check_hash_exist(bkup_rf_path_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
"""
		org_rf_path_1, bkup_rf_path_1, new_org_sample_bam_1, new_org_sample_md5_1, new_bkup_sample_bam_1, new_bkup_sample_md5_1 = scenario_1_fixture()
		org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2 = scenario_2_fixture()
		org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3 = scenario_3_fixture()
		org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4 = scenario_4_fixture()
		org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5 = scenario_5_fixture()
		org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 = scenario_6_fixture()
		org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7 = scenario_7_fixture()
		org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 = scenario_8_fixture()
		org_rf_path_9, bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_sample_bam_9 = scenario_9_fixture()
"""