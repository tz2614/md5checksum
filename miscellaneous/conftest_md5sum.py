#!usr/bin/python

import pytest
import os
import shutil

"""
@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
"""

@pytest.yield_fixture(scope="module")
def make_test_directory(directory):

	"""
    Set up and tear down test directory for each scenario
    """

    # If the directory already exists then error
	assert not os.path.exists(directory), "The test directory {} already exists".format(directory)

    # Otherwise make it in preparation for testing
	new_org_rf = os.path.abspath(os.path.join(directory, "original"))
	new_bkup_rf = os.path.abspath(os.path.join(directory, "backup"))
	os.mkdir(new_org_rf)
	os.mkdir(new_bkup_rf)

	assert os.path.exists(new_org_rf), "The new original runfolder {} cannot be created".format(directory)
	assert os.path.exists(new_bkup_rf), "The new backup runfolder {} cannot be created".format(directory)

	# This gets passed to the test function
	yield new_org_rf, new_bkup_rf

	shutil.rmtree(new_org_rf)
	shutil.rmtree(new_bkup_rf)

	# This runs after the test function is complete to clean up
	# It deletes the test directory we created and anything it contains

"""
@pytest.yield_fixture()	
def test_make_bam_file():
	assert not make_bam_file(org_rf, bkup_rf, new_org_rf, new_bkup_rf, bam_filename)
"""

@pytest.yield_fixture(scope="module")	
def make_bam_file(org_rf, bkup_rf, new_org_rf, new_bkup_rf, bam_name):

	"""
	make associated bam files for each scenario
	"""

	# check if the directory we copying from already exist
	assert os.path.exists(org_rf), "source directory for original runfolder {} DO NOT exists".format(org_rf)
	assert os.path.exists(bkup_rf), "source directory for backup runfolder {} DO NOT exists".format(bkup_rf)

	#create the path of the files
	org_bam = os.path.join(org_rf, bam_name)
	bkup_bam = os.path.join(bkup_rf, bam_name)

	#check if the bam files we are copying exists
	assert os.path.exists(org_bam), "The bam {} we wish to copy DO NOT exists".format(org_bam)
	assert os.path.exists(bkup_bam), "The bam {} we wish to copy DO NOT exists".format(bkup_bam)

	new_org_bam = os.path.join(new_org_rf, bam_name)
	new_bkup_bam = os.path.join(new_bkup_rf, bam_name)

	#copy the files from specified directory	
	shutil.copyfile(org_bam, new_org_bam)
	shutil.copyfile(bkup_bam, new_bkup_bam)

	# Check that the new file exists
	assert os.path.exists(new_org_bam), "The new copy of bam {} DO NOT exists".format(new_org_bam)
	assert os.path.exists(new_bkup_bam), "The new copy of bam {} DO NOT exists".format(new_bkup_bam)

	yield org_bam, bkup_bam, new_org_bam, new_bkup_bam
	# This gets passed to the test function

	# This runs after the test function is complete to clean up
	# It deletes the test bam file we created
	os.remove(new_org_bam)
	os.remove(new_bkup_bam)

@pytest.yield_fixture(scope="module")	
def make_md5_file(org_bam, bkup_bam, new_org_bam, new_bkup_bam):

	"""make associated md5 files for each scenario"""

	# create the path of the files

	org_md5 = org_bam + ".md5"
	bkup_md5 = bkup_bam + ".md5"

	# check the md5 files we care trying to copy exist

	assert os.path.exists(org_md5), "The md5 {} we wish to copy DO NOT exists".format(org_md5)
	assert os.path.exists(bkup_md5), "The md5 {} we wish to copy DO NOT exists".format(bkup_md5)

	new_org_md5 = new_org_bam + ".md5"
	new_bkup_md5 = new_bkup_bam + ".md5"

	shutil.copyfile(bkup_md5, new_bkup_md5)
	shutil.copyfile(org_md5, new_org_md5)

	# Check that the new file exists
	assert os.path.exists(new_org_md5), "The new copy of md5 {} DO NOT exists".format(new_bkup_md5)
	assert os.path.exists(new_bkup_md5), "The new copy of md5 {} DO NOT exists".format(new_bkup_md5)

	yield org_md5, bkup_md5, new_org_md5, new_bkup_md5
	# This gets passed to the test function

	# This runs after the test function is complete to clean up
	# It deletes the test md5 file we created
	os.remove(new_org_md5)
	os.remove(new_bkup_md5)
	
