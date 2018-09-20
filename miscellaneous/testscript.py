#!usr/bin/python

import md5sumscript_7
import pytest
import glob
import random

"""
class Test_md5sumscript_7(object):

	def __init__(self, rf_path):
		self.rf_path = rf_path

	def __init__(self, bam_path):
		self.bam_path = bam_path

	def __init__(self, md5_path):
		self.md5_path = md5_path

	def __init__(self, create_list):
		self.create_list = create_list

	def __init__(self, check_list):
		self.check_list = check_list

	def __init__(self, checkfilepath):
		self.checkfilepath = checkfilepath

	def __init__(self, bam_filename):
		self.bam_filename = bam_filename

	def __init__(self, md5_filename):
		self.md5_filename = md5_filename

	def __init__(self, check_dict):
		self.check_dict = check_dict

	def __init__(self,org_rf_path):
		self.org_rf_path = org_rf_path

	def __init__(self, bkup_rf_path):
		self.bkup_rf_path = bkup_rf_path

	def __init__(self, org_bkup_check_dict):
		self.org_bkup_check_dict = org_bkup_check_dict

	assert (rf_path.startswith("/mnt/storage/data/NGS") or runfolders.startswith("/mnt/archive/data/NGS")), "runfolder given incorrect"
"""

#machine_letter = random.choice(string.ascii_uppercase)
#machine_number = "".join(random.choice(string.digits) for x in range(5))
#date_number = "".join(random.choice(string.digits) for x in range(6))
#sample_letter = random.choice(string.ascii_uppercase)
#sample_number = "".join(random.choice(string.digits) for x in range(6))
#bam_content = "".join(random.choice(string.ascii_letters for x in range(1000)))

"""
def test_rf_path_exist(create_):
	assert os.path.exist(create_org_runfolder), "runfolder path DO NOT exist"

def test_rf_path_is_runfolder(create_org_runfolder):
	assert create_org_runfolder.split("/")[-3] == create_runfolder_name
	assert os.path.isdir(create_org_runfolder), "runfolder path is NOT a directory"
	
#conftest setup tear down setup for md5 check program testing

#!usr/bin/python

import pytest
import os
import shutil


current_directory = os.getcwd()

#setup a test_runfolder
@pytest.fixture()
def create_runfolder_name():
	
	machine_letter = "K"
	machine_number = "00001"
	date_number = "123456"
	return date_number + "_" + machine_letter + machine_number

@pytest.fixture()
def create_diff_runfolder_name(create_runfolder_name):

	diff_runfolder_name = create_runfolder_name[:-1] + "9"
	return diff_runfolder_name

@pytest.fixture()
def create_sample_name():

	sample_letter = "X"
	sample_number = "000001"
	return sample_letter + sample_number

@pytest.fixture()
def create_diff_sample_name(create_sample_name):

	diff_sample_name = create_sample_name[:-1] + "2"
	return diff_sample_name

@pytest.fixture()
def create_org_runfolder(current_directory):

	org_runfolder = os.path.join(current_directory, "original", "{}".format(create_runfolder_name), "bams")
	if not os.path.exist(org_runfolder):
		os.makedirs(org_runfolder)
		
	def fin():
		print ("teardown org_runfolder")
		shutil.rmtree(org_runfolder)
	
	current_directory.addfinalizer(fin)
	return os.path.abspath(org_runfolder)

@pytest.fixture()
def create_bkup_runfolder(current_directory):
	bkup_runfolder = os.path.join(current_directory, "backup", "{}".format(create_runfolder_name), "bams")
	if not os.path.exist(bkup_runfolder):
		os.makedirs(bkup_runfolder)
		
	def fin():
		print ("teardown bkup_runfolder")
		shutil.rmtree(bkup_runfolder)
	
	current_directory.addfinalizer(fin)
	return os.path.abspath(bkup_runfolder)

@pytest.fixture()
def create_bam_in_org(create_org_runfolder):

	test_bam_filename = create_sample_name() + ".bam"
	bam_file_path = os.path.join(create_org_runfolder(current_directory), test_bam_filename)
	if not os.path.exist(bam_file_path):
		with open(bam_file_path, "w") as f:
			bam_content = "0123456789abcdefghijklmnopqrstuvwxyz"
			f.write(bam_content)

	def fin():
		print "tear down original test_bam" 
		os.remove(bam_file_path)
	return bam_file_path

@pytest.fixture()
def create_diff_bam_in_org(create_bam_in_org):

	if not os.path.exist(create_bam_in_org):
		with open(create_bam_in_org, "w") as f:
			bam_content = "0123456789abcdefghijklmnopqrstuvwxy0"
			f.write(bam_content)
	def fin():
		print "tear down different original test_bam" 
		os.remove(create_bam_in_org)
	return create_bam_in_org

@pytest.fixture()
def create_bam_in_bkup(create_bkup_runfolder):

	test_bam_filename = create_sample_name() + ".bam"
	bam_file_path = os.path.join(create_bkup_runfolder(current_directory), test_bam_filename)
	if not os.path.exist(bam_file_path):
		with open(bam_file_path, "w") as f:
			bam_content = "0123456789abcdefghijklmnopqrstuvwxyz"
			f.write(bam_content)

	def fin():
		print "tear down backup test_bam" 
		os.remove(bam_file_path)
	return bam_file_path

@pytest.fixture()
def create_diff_bam_in_bkup(create_bam_in_bkup):

	if not os.path.exist(create_bam_in_bkup):
		with open(create_bam_in_bkup, "w") as f:
			bam_content = "0123456789abcdefghijklmnopqrstuvwxy0"
			f.write(bam_content)
	def fin():
		print "tear down different backup test_bam" 
		os.remove(create_bam_in_bkup)
	return create_bam_in_bkup

@pytest.fixture()
def create_md5_in_org(create_bam_in_org):
	test_md5_filename = create_bam_in_org + ".md5"
	if not os.path.exist(test_md5_filename):
		with open(md5_file_path, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012345"
			f.write(md5_content)
	def fin():
		print "tear down original test_md5" 
		os.remove(test_md5_filename)
	return test_md5_filename

@pytest.fixture()
def create_diff_md5_in_org(create_md5_in_org):

	if not os.path.exist(create_md5_in_org):
		with open(create_md5_in_org, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012346"
			f.write(md5_content)
	def fin():
		print "tear down different original test_md5" 
		os.remove(create_md5_in_org)
	return create_md5_in_org

@pytest.fixture()
def create_md5_in_bkup(create_bam_in_bkup):
	test_md5_filename = create_bam_in_bkup + ".md5"
	if not os.path.exist(test_md5_filename):
		with open(test_md5_filename, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012345"
			f.write(md5_content)
	def fin():
		print "tear down backup test_md5" 
		os.remove(test_md5_filename)
	return test_md5_filename

@pytest.fixture()
def create_diff_md5_in_bkup(create_md5_in_bkup):

	if not os.path.exist(create_md5_in_bkup):
		with open(create_md5_in_org, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012346"
			f.write(bam_content)
	def fin():
		print "tear down different backup test_md5" 
		os.remove(create_md5_in_bkup)
	return create_md5_in_bkup

@pytest.mark.usefixtures("create_runfolder_name","create_sample_name", "create_org_runfolder", "create_bam_in_org", "create_md5_in_org")


@pytest.fixture()
def runfolder1(org_rf_path1, bkup_rf-path1):
	bam_list1, md5_list1 = md5sumscript.create_two_lists(org_rf_path1)
	org_bam_list1, org_md5_list1 = md5sumscript.create_two_lists(org_rf_path1)
	bkup_bam_list1, bkup_md5_list1 = md5sumscript.create_two_lists(bkup_rf_path1)

    #create md5_missing log files
    org_log_file1 = md5sumscript.create_md5_missing_logfile(orf_rf_path1)
    bkup_log_file1 = create_md5_missing_logfile(bkup_rf_path1)

    #check list of bam files to see if .md5 files for each bam file is present, if not generate it.
    new_md5_list_in_org1 = create_md5(org_bam_list1, org_md5_list1, org_log_file1)
    new_md5_list_in_bkup1 = create_md5(bkup_bam_list1, bkup_md5_list1, bkup_log_file1)

    #create the chk log files
    org_log_file1 = create_logfile(org_rf_path1)
    bkup_log_file1 = create_logfile(bkup_rf_path1)

    #create a dictionary containing the md5 filenames and its associated md5 hash
    org_bkup_check_dict1 = create_check_dict(org_log_file1, bkup_log_file1, new_md5_list_in_org1, new_md5_list_in_bkup1)

    #check md5sum values and bam filenames within .md5 match between original and backup runfolder
    check_org_bkup(org_rf_path, bkup_rf_path, org_bkup_check_dict)

@pytest.fixture()
def generate_bkup_rf_path():

	bkup_runfolder = "/mnt/storage/home/zhengt/projects/md5checksum/testrunfolders/backup"
	return os.path.abspath(bkup_runfolder)


@pytest.fixture()
def create_md5_in_org(generate_org_rf_path):
	test_md5_filename = create_bam_in_org + ".md5"
	if not os.path.exist(test_md5_filename):
		with open(md5_file_path, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012345"
			f.write(md5_content)
	def fin():
		print "tear down original test_md5" 
		os.remove(test_md5_filename)
	return test_md5_filename

@pytest.fixture()
def create_diff_md5_in_org(create_md5_in_org):

	if not os.path.exist(create_md5_in_org):
		with open(create_md5_in_org, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012346"
			f.write(md5_content)
	def fin():
		print "tear down different original test_md5" 
		os.remove(create_md5_in_org)
	return create_md5_in_org

@pytest.fixture()
def create_md5_in_bkup(create_bam_in_bkup):
	test_md5_filename = create_bam_in_bkup + ".md5"
	if not os.path.exist(test_md5_filename):
		with open(test_md5_filename, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012345"
			f.write(md5_content)
	def fin():
		print "tear down backup test_md5" 
		os.remove(test_md5_filename)
	return test_md5_filename

@pytest.fixture()
def create_diff_md5_in_bkup(create_md5_in_bkup):

	if not os.path.exist(create_md5_in_bkup):
		with open(create_md5_in_org, "w") as f:
			md5_content = "abcdefghijklmnopqrstuvwxyz012346"
			f.write(bam_content)
	def fin():
		print "tear down different backup test_md5" 
		os.remove(create_md5_in_bkup)
	return create_md5_in_bkup

@pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture")
def test_create_md5_missing_logfile():

	

	rf_path_list = [org_rf_path_1, org_rf_path_2, org_rf_path_3, org_rf_path_4, org_rf_path_5, org_rf_path_6, org_rf_path_7, org_rf_path_8, org_rf_path_9, bkup_rf_path_1, bkup_rf_path_2, bkup_rf_path_3, bkup_rf_path_4, bkup_rf_path_5, bkup_rf_path_6, bkup_rf_path_7, bkup_rf_path_8, bkup_rf_path_9]
	#md5_missing_log_list = []

	for rf_path in rf_path_list:

		log_file = md5sumscript.create_md5_missing_logfile(rf_path)

		if log_file == rf_path + "md5_missing.txt":
			print ("{} path generated correct".format(log_file))
			#md5_missing_log_list.append(log_file)

		else:
			print ("{} path generated wrong".format(log_file))

	return md5_missing_log_list

	def test_create_new_md5_file(new_md5_list):

		for md5 in new_md5_list:

			assert os.path.exists(md5), "new md5 did not get generated"

	def test_check_hash_format():

		with open (new_org_sample_md5_1, "r") as md5_file:
			checksum = md5_file.readline().strip()[:32]
		
		for checksum in check_dict.values():

			chars = ""

			try:
				for char in checksum:
					if char in string.ascii_letters() or char in string.digits():
						chars += char
			except:
				print ("characters in checksum not in correct format")
				return None

	def test_check_md5(checkfilelist, md5_list):

		#for checksum in check_dict.values():
		md5_hashes = []
		md5_filenames = []

		for md5 in md5_list:

			with open (md5, "r") as md5_file:
				if len(md5_file.readline().split("  ")) == 2:
					bam_filename = md5_file.readline().split("  ")[-1]
				else:
					if not md5_file.readline()[32:]:
						bam = "None"
					else:
						bam = ".".join(md5.split("/")[-1].split(".")[:-1])
				
				md5_hash = md5_file.readline()[:32]
				md5_filename = md5.split("/")[-1]

				assert md5_filename in org_check_dict.keys() or bkup_check_dict, "md5_filename not in check_dict, check_md5 function NOT working"

pytest.mark.usefixtures("scenario_1_fixture", "scenario_2_fixture", "scenario_3_fixture", "scenario_4_fixture", "scenario_5_fixture", "scenario_6_fixture", "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture")
"""

@pytest.yield_fixture
def scenario_2_fixture(scope="class"):

	"""
    Set up and tear down test directory2 for scenario2
    """

		# if the directory already exist then error
		assert not os.path.exists(directory2), "The test directory {} already exists".format(directory2)

		# Otherwise make it in preparation for testing
		org_rf_path = os.path.abspath(os.path.join(directory2, "/original/"))
		bkup_rf_path = os.path.abspath(os.path.join(directory2, "/backup/"))
		os.makedirs(org_runfolder)
		os.makedirs(bkup_runfolder)


	org_sample_bam = os.path.join(org_rf_path2, "sample2.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory2, "sample2.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path2, "sample2.bam")
	bkup_sample_md5 = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory2, "sample2.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2  # This gets passed to the test function
	
    
	shutil.rmtree(directory2)

	#return org_rf_path_2, bkup_rf_path_2, new_org_sample_bam_2, new_org_sample_md5_2, new_bkup_sample_bam_2, new_bkup_sample_md5_2

@pytest.yield_fixture
def scenario_3_fixture(scope="class"):

	"""
    Set up and tear down test directory3 for scenario3
    """


	# if the directory already exist then error
	assert not os.path.exists(directory3), "The test directory {} already exists".format(directory3)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory3, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory3, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path2, "sample3.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory3, "sample3.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path2, "sample3.bam")
	bkup_sample_md5 = org_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory3, "sample3.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3  # This gets passed to the test function
	
	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory3)

	#return org_rf_path_3, bkup_rf_path_3, new_org_sample_bam_3, new_org_sample_md5_3, new_bkup_sample_bam_3, new_bkup_sample_md5_3

@pytest.yield_fixture
def scenario_4_fixture(scope="class"):

	"""
    Set up and tear down test directory4 for scenario4
    """


	# if the directory already exist then error
	assert not os.path.exists(directory4), "The test directory {} already exists".format(directory4)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory4, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory4, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path1, "sample1.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory4, "sample1.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path1, "sample1.bam")
	bkup_sample_md5 = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory4, "sample1.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4  # This gets passed to the test function
	
	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory4)

	#return org_rf_path_4, bkup_rf_path_4, new_org_sample_bam_4, new_org_sample_md5_4, new_bkup_sample_bam_4, new_bkup_sample_md5_4

@pytest.yield_fixture
def scenario_5_fixture(scope="class"):

	"""
    Set up and tear down test directory5 for scenario5
    """


	# if the directory already exist then error
	assert not os.path.exists(directory5), "The test directory {} already exists".format(directory5)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory5, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory5, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path1, "sample2.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory5, "sample2.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path1, "sample2.bam")
	bkup_sample_md5 = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory5, "sample2.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5  # This gets passed to the test function
	
	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory5)

	#return org_rf_path_5, bkup_rf_path_5, new_org_sample_bam_5, new_org_sample_md5_5, new_bkup_sample_bam_5, new_bkup_sample_md5_5

@pytest.yield_fixture
def scenario_6_fixture(scope="class"):

	"""
    Set up and tear down test directory6 for scenario6
    """


	# if the directory already exist then error
	assert not os.path.exists(directory5), "The test directory {} already exists".format(directory6)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory6, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory6, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path1, "sample3.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory6, "sample3.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path1, "sample3.bam")
	bkup_sample_md5 = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory6, "sample3.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6  # This gets passed to the test function
	
	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory6)

	#return org_rf_path_6, bkup_rf_path_6, new_org_sample_bam_6, new_org_sample_md5_6, new_bkup_sample_bam_6, new_bkup_sample_md5_6 

@pytest.yield_fixture
def scenario_7_fixture(scope="class"):

	"""
    Set up and tear down test directory7 for scenario7
    """

    def _make_directory()
	# if the directory already exist then error
	assert not os.path.exists(directory5), "The test directory {} already exists".format(directory7)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory7, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory7, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path3, "sample11.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory7, "sample11.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)
	shutil.copyfile(org_sample_md5, new_org_sample_md5)

	bkup_sample_bam = os.path.join(bkup_rf_path3, "sample11.bam")
	bkup_sample_bam = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory7, "sample11.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)

	yield org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7  # This gets passed to the test function
	
	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory7)

	#return org_rf_path_7, bkup_rf_path_7, new_org_sample_bam_7, new_org_sample_md5_7, new_bkup_sample_bam_7, new_bkup_sample_md5_7

@pytest.yield_fixture
def scenario_8_fixture(scope="class"):

	"""
    Set up and tear down test directory8 for scenario8
    """


	# if the directory already exist then error
	assert not os.path.exists(directory8), "The test directory {} already exists".format(directory8)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory5, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory4, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path3, "sample12.bam")
	org_sample_md5 = org_sample_bam + ".md5"
	new_org_sample_bam = os.path.join(directory8, "sample12.bam")
	new_org_sample_md5 = new_org_sample_bam + ".md5"

	shutil.copyfile(org_sample_bam, new_org_sample_bam)

	bkup_sample_bam = os.path.join(bkup_rf_path3, "sample12.bam")
	bkup_sample_md5 = bkup_sample_bam + ".md5"
	new_bkup_sample_bam = os.path.join(directory8, "sample12.bam")
	new_bkup_sample_md5 = new_bkup_sample_bam + ".md5"

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)
	shutil.copyfile(bkup_sample_md5, new_bkup_sample_md5)

	yield org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_org_sample_md5_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8  # This gets passed to the test function

	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory8)

	#return org_rf_path_8, bkup_rf_path_8, new_org_sample_bam_8, new_org_sample_md5_8, new_bkup_sample_bam_8, new_bkup_sample_md5_8 

@pytest.yield_fixture
def scenario_9_fixture(scope="class"):

	"""
    Set up and tear down test directory9 for scenario9
    """

	# if the directory already exist then error
	assert not os.path.exists(directory9), "The test directory {} already exists".format(directory9)

	# Otherwise make it in preparation for testing
	org_rf_path = os.path.abspath(os.path.join(directory9, "/original/"))
	bkup_rf_path = os.path.abspath(os.path.join(directory9, "/backup/"))
	os.makedirs(org_runfolder)
	os.makedirs(bkup_runfolder)

	org_sample_bam = os.path.join(org_rf_path3, "sample13.bam")
	new_org_sample_bam = os.path.join(directory9, "sample13.bam")

	shutil.copyfile(org_sample_bam, new_org_sample_bam)

	bkup_sample_bam = os.path.join(bkup_rf_path3, "sample13.bam")
	new_bkup_sample_bam = os.path.join(directory9, "sample13.bam")

	shutil.copyfile(bkup_sample_bam, new_bkup_sample_bam)

	yield org_rf_path_9, bkup_rf_path_9, new_org_sample_bam_9, new_org_sample_md5_9, new_bkup_sample_bam_9, new_bkup_sample_md5_9  # This gets passed to the test function

	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory9)

	org_md5_lists = [org_md5_list_1, org_md5_list_2, org_md5_list_3, org_md5_list_4, org_md5_list_5, org_md5_list_6, org_md5_list_7, org_md5_list_8, org_md5_list_9, new_org_md5_list_1, new_org_md5_list_2, new_org_md5_list_3, new_org_md5_list_4, new_org_md5_list_5, new_org_md5_list_6, new_org_md5_list_7, new_org_md5_list_8, new_org_md5_list_9]
	bkup_md5_lists = [bkup_md5_list_1, bkup_md5_list_2, bkup_md5_list_3, bkup_md5_list_4, bkup_md5_list_5, bkup_md5_list_6, bkup_md5_list_7, bkup_md5_list_8, bkup_md5_list_9, new_bkup_md5_list_1, new_bkup_md5_list_2, new_bkup_md5_list_3, new_bkup_md5_list_4, new_bkup_md5_list_5, new_bkup_md5_list_6, new_bkup_md5_list_7, new_bkup_md5_list_8, new_bkup_md5_list_9]
	check_dicts = [check_dict_1, check_dict_2, check_dict_3, check_dict_4, check_dict_5, check_dict_6, check_dict_7, check_dict_8, check_dict_9]

	md5_list = [new_org_md5_1, new_org_md5_2, new_org_md5_3, new_org_md5_4, new_org_md5_5, new_org_md5_6, new_org_md5_7, new_bkup_md5_1, new_bkup_md5_2, new_bkup_md5_3, new_bkup_md5_4, new_bkup_md5_5, new_bkup_md5_6, new_bkup_md5_8]

	assert os.path.exists(md5_path), "md5_path DO NOT exist"
    md5_path = os.path.abspath(md5_path)
    assert os.path.isabs(md5_path), "md5_path NOT absolute"

	org_bkup_dict_2 = {"sample2.bam.md5" : "15f1891487fd6b26f752b50468adb49f"}
	org_dict_3 = {"sample3.bam.md5" : "15f1891487fd6b26f752b50468adb59f"}
	bkup_dict_3 = {"sample3.bam.md5" : "15f1891487fd6b26f752b50468adb59f%£"}
	org_bkup_dict_5 = {"sample2.bam.md5" : "0cc1f1cc52cc2d0ed218337cf947eeb8"}				
	org_dict_6 = {"sample3.bam.md5" : "a5119b252ab16786e583b550fab714ac"}
	bkup_dict_6 = {"sample3.bam.md5" : "a5119b252ab16786e583b550fab714ad"}
	org_bkup_dict_8 = {"sample1.bam.md5" : "38f7c7e572fe7aeffe4fcf5728c31f5d"}

	assert org_check_dict_2.items() == org_bkup_dict_2.items(), "md5 filename and hash not present == org case 2"
	assert bkup_check_dict_2.items() == org_bkup_dict_2.items(), "md5 filename and hash not present == bkup case 2"
	assert org_check_dict_3.items() == org_dict_3.items(), "md5 filename and hash not present == org case 3"
	assert bkup_check_dict_3.items() == bkup_dict_3.items(), "md5 filename and hash not present == bkup case 3"
	assert org_check_dict_5.items() == org_bkup_dict_5.items(), "md5 filename and hash not present == org case 5"
	assert bkup_check_dict_5.items() == org_bkup_dict_5.items(), "md5 filename and hash not present == bkup case 5"
	assert org_check_dict_6.items() == org_bkup_dict_6.items(), "md5 filename and hash not present == org case 6"
	assert bkup_check_dict_6.items() == org_bkup_dict_6.items(), "md5 filename and hash not present == bkup case 6"
	assert org_check_dict_8.items() == org_bkup_dict_8.items(), "md5 filename and hash not present for case 7"
	assert bkup_check_dict_8.items() == org_bkup_dict_8.items(), "md5 filename and hash not present for case 8"

				elif line.startswith("md5sum:") and ("sample22.bam") in line and "No such file or directory" in line:
					print ("md5sum -c program executed for {}, bam file stated does NOT exist".format("sample22.bam"))

				elif line.startswith("sample22.bam") and "FAILED open or read" in line:
					print ("md5sum -c program executed for {}, bam file cannot be opened or read".format("sample22.bam"))

				elif line.startswith("sample12.bam") and "OK" in line:
					print ("{} recorded in log file, and hash match".format("sample12.bam"))

@pytest.yield_fixture
def scenario_10_fixture():

	"""
    Set up and tear down test directory10 for scenario10
    """

	# if the directory already exist then error
	assert not os.path.exists(directory10), "The test directory {} already exists".format(directory10)

	# Otherwise make it in preparation for testing
	new_org_rf_path_10 = os.path.abspath(os.path.join(directory10, "/original/"))
	new_bkup_rf_path_10 = os.path.abspath(os.path.join(directory10, "/backup/"))
	os.makedirs(new_org_rf_path_10)
	os.makedirs(new_bkup_rf_path_10)

	org_bam_10 = os.path.join(org_rf_path3, bam_name6)
	new_org_bam_10 = os.path.join(directory10, bam_name6)

	shutil.copyfile(org_bam_10, new_org_bam_10)

	bkup_bam_10 = os.path.join(bkup_rf_path3, bam_name6)
	new_bkup_bam_10 = os.path.join(directory10, bam_name6)

	shutil.copyfile(bkup_bam_10, new_bkup_bam_10)

	yield new_org_rf_path_10, new_bkup_rf_path_10, new_org_bam_10, new_bkup_bam_10 # This gets passed to the test function

	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains
	shutil.rmtree(directory10)


"""
    new_org_rf_path_1, new_bkup_rf_path_1, new_org_bam_1, new_org_md5_1, new_bkup_bam_1, new_bkup_md5_1 = scenario_1_fixture()
	new_org_rf_path_2, new_bkup_rf_path_2, new_org_bam_2, new_org_md5_2, new_bkup_bam_2, new_bkup_md5_2 = scenario_2_fixture()
	new_org_rf_path_3, new_bkup_rf_path_3, new_org_bam_3, new_org_md5_3, new_bkup_bam_3, new_bkup_md5_3 = scenario_3_fixture()
	new_org_rf_path_4, new_bkup_rf_path_4, new_org_bam_4, new_org_md5_4, new_bkup_bam_4, new_bkup_md5_4 = scenario_4_fixture()
	new_org_rf_path_5, new_bkup_rf_path_5, new_org_bam_5, new_org_md5_5, new_bkup_bam_5, new_bkup_md5_5 = scenario_5_fixture()
	new_org_rf_path_6, new_bkup_rf_path_6, new_org_bam_6, new_org_md5_6, new_bkup_bam_6, new_bkup_md5_6 = scenario_6_fixture()
	new_org_rf_path_7, new_bkup_rf_path_7, new_org_bam_7, new_org_md5_7, new_bkup_bam_7 = scenario_7_fixture()
	new_org_rf_path_8, new_bkup_rf_path_8, new_org_bam_8, new_bkup_bam_8, new_bkup_md5_8 = scenario_8_fixture()
    new_org_rf_path_9, new_bkup_rf_path_9, new_org_sample1_bam_9, new_bkup_bam_9 = scenario_9_fixture()

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

    new_md5_list1 = md5sumscript.create_md5(bam_list1, org_rf_path_1)
    new_md5_list7 = md5sumscript.create_md5(bam_list7, org_rf_path_7)
    new_md5_list8 = md5sumscript.create_md5(bam_list8, org_rf_path_8)
    new_md5_list9 = md5sumscript.create_md5(bam_list9, org_rf_path_9)

    md5_list = [new_org_md5_1, new_org_md5_2, new_org_md5_3, new_org_md5_4, new_org_md5_5, new_org_md5_6, new_org_md5_7, new_bkup_md5_1, new_bkup_md5_2, new_bkup_md5_3, new_bkup_md5_4, new_bkup_md5_5, new_bkup_md5_6, new_bkup_md5_8]
    
    check_dict = md5sumscript.create_check_dict(orgfilepath, bkupfilepath, org_md5_list, bkup_md5_list)
"""



new_org_bam_list_6, new_org_md5_list_6 = md5sumscript.create_two_lists(new_org_rf_6)
new_bkup_bam_list_6, new_bkup_md5_list_6 = md5sumscript.create_two_lists(new_bkup_rf_6)

, scenario_7_fixture, scenario_8_fixture, scenario_9_fixture
, "scenario_7_fixture", "scenario_8_fixture", "scenario_9_fixture"

	"""
	using scenarios 6-9, set up the directories, bam + md5 files, log files and perform a check on the md5s within the directories and md5 filename and hash in org_bkup_check_dict (nested diictionary).
	using the check_md5filename, compare_md5hash, check_hash_exist function, perform a comparison between the md5 hash between original runfolder and the backup runfolder, 
	and create 4 dictionaries which sorts the data into 4 categories. The content of each dictionary is checked by test_final_four_dicts function
	"""

	

	md5_list = [new_org_md5_6, new_org_md5_7, new_bkup_md5_6, new_bkup_md5_8]

	new_org_rf_path_7, new_bkup_rf_path_7, new_org_bam_7, new_org_md5_7, new_bkup_bam_7 = scenario_7_fixture()

	check_dict_7 = {}
	
	md5_matches_6, md5_mismatches_6, md5_in_org_not_bkup_6, md5_in_bkup_not_org_6 = md5sumscript.check_org_bkup(new_org_rf_path_6, new_bkup_rf_path_6, check_dict_6)
	md5_matches_7, md5_mismatches_7, md5_in_org_not_bkup_7, md5_in_bkup_not_org_7 = md5sumscript.check_org_bkup(new_org_rf_path_7, new_bkup_rf_path_7, check_dict_7)
	md5_matches_8, md5_mismatches_8, md5_in_org_not_bkup_8, md5_in_bkup_not_org_8 = md5sumscript.check_org_bkup(new_org_rf_path_8, new_bkup_rf_path_8, check_dict_8)
	md5_matches_9, md5_mismatches_9, md5_in_org_not_bkup_9, md5_in_bkup_not_org_9 = md5sumscript.check_org_bkup(new_org_rf_path_9, new_bkup_rf_path_9, check_dict_9)

	new_org_md5_list_6 = md5sumscript.create_md5(org_bam_list_6, new_org_rf_6)
	new_org_md5_list_7 = md5sumscript.create_md5(org_bam_list_7, new_org_rf_7)
	new_org_md5_list_8 = md5sumscript.create_md5(org_bam_list_8, new_org_rf_8)
	new_bkup_md5_list_6 = md5sumscript.create_md5(bkup_bam_list_6, new_bkup_rf_6)
	new_bkup_md5_list_7 = md5sumscript.create_md5(bkup_bam_list_7, new_bkup_rf_7)
	new_bkup_md5_list_8 = md5sumscript.create_md5(bkup_bam_list_8, new_bkup_rf_8)


	check_dict_6 = md5sumscript.create_check_dict(org_checkfilepath_6, bkup_checkfilepath_6, new_org_md5_list_6, new_bkup_md5_list_6, check_dict_6)
	check_dict_7 = md5sumscript.create_check_dict(org_checkfilepath_7, bkup_checkfilepath_7, new_org_md5_list_7, new_bkup_md5_list_7, check_dict_7)
	check_dict_8 = md5sumscript.create_check_dict(org_checkfilepath_8, bkup_checkfilepath_8, new_org_md5_list_8, new_bkup_md5_list_8, check_dict_8)
	check_dict_9 = md5sumscript.create_check_dict(org_checkfilepath_9, bkup_checkfilepath_9, new_org_md5_list_9, new_bkup_md5_list_9, check_dict_9)

	md5_matches_6, md5_mismatches_6, md5_in_org_not_bkup_6, md5_in_bkup_not_org_6 = md5sumscript.check_org_bkup(new_org_rf_path_6, new_bkup_rf_path_6, check_dict_6)
	md5_matches_7, md5_mismatches_7, md5_in_org_not_bkup_7, md5_in_bkup_not_org_7 = md5sumscript.check_org_bkup(new_org_rf_path_7, new_bkup_rf_path_7, check_dict_7)
	md5_matches_8, md5_mismatches_8, md5_in_org_not_bkup_8, md5_in_bkup_not_org_8 = md5sumscript.check_org_bkup(new_org_rf_path_8, new_bkup_rf_path_8, check_dict_8)
	md5_matches_9, md5_mismatches_9, md5_in_org_not_bkup_9, md5_in_bkup_not_org_9 = md5sumscript.check_org_bkup(new_org_rf_path_9, new_bkup_rf_path_9, check_dict_9)

	for md5 in org_md5_list_6:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_org_rf_6, md5_filename, check_dict_6["storage"]), "md5 NOT in original runfolder"

	for md5 in bkup_md5_list_6:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_bkup_rf_6, md5_filename, check_dict_6["archive"]), "md5 NOT in backup runfolder"

	for md5 in org_md5_list_8:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_org_rf_8, md5_filename, check_dict_8["storage"]), "md5 NOT in original runfolder"
	
	for md5 in bkup_md5_list_8:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_bkup_rf_8, md5_filename, check_dict_8["archive"]), "md5 NOT in backup runfolder"
	
	for md5 in org_md5_list_9:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_org_rf_9, md5_filename, check_dict_9["storage"]), "md5 NOT in original runfolder"

	for md5 in bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_bkup_rf_9, md5_filename, check_dict_9["archive"]), "md5 NOT in backup runfolder"

	for md5 in new_org_md5_list_9:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_org_rf_9, md5_filename, check_dict_9["storage"]), "md5 NOT in original runfolder"

	for md5 in new_bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_bkup_rf_9, md5_filename, check_dict_9["archive"]), "md5 NOT in backup runfolder"

	for md5 in bkup_md5_list_7:
		md5_filename = md5.split("/")[-1]
		assert md5_filename in md5sumscript.check_md5filename(new_bkup_rf_7, md5_filename, check_dict_7["archive"]), "md5 NOT in backup runfolder"

for md5 in org_md5_list_1:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_1, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_1, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_1:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_1, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_1, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in org_md5_list_2:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_2, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_2, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_2:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_2, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_2, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in org_md5_list_3:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_3, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_3, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_3:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_3, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_3, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in org_md5_list_4:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_4, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_4, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_4:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_4, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_4, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in org_md5_list_5:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_5, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_5, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_5:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_5, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_5, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

for md5 in org_md5_list_7:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_7, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_7, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"
	
	for md5 in bkup_md5_list_7:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_7, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_7, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in org_md5_list_9:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in new_org_md5_list_9:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_org_rf_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_org_rf_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in new_bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_9, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkup_rf_9, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

	for md5 in bkup_md5_list_7:
		md5_filename = md5.split("/")[-1]
		if check_dict["storage"][md5_filename] == check_dict["archive"][md5_filename]:
			assert md5sumscript.compare_md5hash(new_bkup_rf_7, md5_filename, check_dict), "hash matching, but output is False, compare_md5hash function NOT working"
		else:
			assert not md5sumscript.compare_md5hash(new_bkuprf_7, md5_filename, check_dict), "hash not matching, but output is True, compare_md5hash function NOT working"

for md5 in org_md5_list_3:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_3, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_3, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_3, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_3, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
	
	for md5 in bkup_md5_list_3:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_3, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_3, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_3, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_3, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_4:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_4, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_4, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_4, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_4, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in bkup_md5_list_4:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_4, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_4, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_4, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"				
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_4, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_5:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_5, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_5, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_5, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_5, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in bkup_md5_list_5:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_5, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_5, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_5, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_5, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_6:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_6, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_6, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_6, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_6, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"
	
	for md5 in bkup_md5_list_6:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_6, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_6, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_6, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_6, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_7:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_7, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_7, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_7, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_7, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in bkup_md5_list_7:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_8:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_8, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_8, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_8, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_8, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in bkup_md5_list_8:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_8, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_8, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_8, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_8, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in org_md5_list_9:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in new_org_md5_list_9:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_org_rf_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in new_bkup_md5_list_9:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_9, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5 in new_bkup_md5_list_7:
		md5_filename = md5.split("/")[-1]

		if check_dict["archive"][md5_filename] in check_dict["storage"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash exist in original, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash do not exist in original, but check_hash_exist function NOT working"

		if check_dict["storage"][md5_filename] in check_dict["archive"].values():
			assert md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash exist in backup, but check_hash_exist function NOT working"
		else:
			assert not md5sumscript.check_hash_exist(new_bkup_rf_7, md5_filename, check_dict), "hash do not exist in backup, but check_hash_exist function NOT working"

	for md5, values in md5_matches_4["storage"].items():
		assert md5 == "sample1.bam.md5" and values == "8620b0a9852e248c88b3f7ed30e73d01"
	for md5, values in md5_matches_4["archive"].items():
		assert md5 == "sample1.bam.md5" and values == "8620b0a9852e248c88b3f7ed30e73d01"

	new_org_rf_path_1 = os.path.join(directory1, "original")
	assert not os.path.exists(new_org_rf_path_1)
	new_bkup_rf_path_1 = os.path.join(directory1, "backup")
	assert not os.path.exists(new_bkup_rf_path_1)
	os.makedirs(new_org_rf_path_1, new_bkup_rf_path_1)

	org_bam_1 = os.path.join(org_rf_path1, bam_name1)
	assert os.path.exists(org_bam_1)
	new_org_bam_1 = os.path.join(directory1, bam_name1)
	assert not os.path.exists(new_org_bam_1)
	shutil.copyfile(org_bam_1, new_org_bam_1)
	assert os.path.exists(new_org_bam_1)

	org_md5_1 = org_bam_1 + ".md5"
	assert os.path.exists(org_md5_1)
	new_org_md5_1 = new_org_bam_1 + ".md5"
	assert not os.path.exists(new_org_md5_1)
	shutil.copyfile(org_md5, new_org_md5)
	assert os.path.exists(new_org_md5_1)

	bkup_bam_1 = os.path.join(bkup_rf_path1, bam_name1)
	assert os.path.exists(bkup_bam_1)
	bkup_md5_1 = bkup_bam_1 + ".md5"
	assert not os.path.exists(new_bkup_bam_1)
	shutil.copyfile(bkup_bam_1, new_bkup_bam_1)
	assert os.path.exists(new_bkup_bam_1)

	new_bkup_bam_1 = os.path.join(directory1, bam_name1)
	assert os.path.exists(bkup_md5_1)
	new_bkup_md5_1 = new_bkup_bam_1 + ".md5"
	assert not os.path.exists(new_bkup_md5_1)
	shutil.copyfile(bkup_md5_1, new_bkup_md5_1)
	assert os.path.exists(new_bkup_md5_1)