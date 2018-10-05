# CBI-5 Programming Project
 - md5sumscript.py
 
By Tengyue Zheng
20/09/2018

## Function:

File integrity checker for bam files in a runfolder using Python 2.7.5

The test bam files are available upon request by email @ tengyue.zheng@addenbrookes.nhs.uk

## User Requirements:
- check file integrity of bam files within the specified runfolder using md5 checksum values.

## Instructions:

Before running the program, please read the following instructions:

1.Navigate to your working directory and create an empty folder called "bam_check". 

2.If possible create a virtual environment, so that you can control the library package available for use. To run the script without testing, standalone python 2.7.5 should be sufficient. The program have not been tested in python 3, but if you wish to, feel free to change the print statements in yours scripts after you have cloned the repository in your local workng directory to test the script in python 3 and above.

a) check you have virtualenv installed
```Bash
$pip freeze
virtualenv==1.10.1
```
if you do not have virtualenv, type 
```Bash 
$pip install virutalenv
```
```Bash
$virtualenv --version
```
check the virutalenv version is 1.10.1 or later

b) create a new virtualenv called "bam_check"
```Bash
$virtualenv bam_check

$virtualenv -p /usr/bin/python bam_check
```

c) activate the virtual environment
```Bash
$ source bam_check/bin/activate
```

d) check you have git installed
```Bash
$ git --version
git version 1.8.3.1
```

3.Clone the repository using git
```Bash
git clone https://github.com/tz2614/md5checksum
or 
git clone https://git.ctrulab.uk/zhengt/md5checksum 
```

- This should create directory called "md5checksum" in your bam_check directory.
- check to make sure the main script called "md5sumscript.py" is present
- If you know where you bam files are located, then try to use the full path to the directory if possible.
- If you only have one runfolder, then I would suggest running md5sumscript_for1runfolder.py located in the /miscellaneous directory instead.

4.Navigate to the directory md5checksum/ and execute the program for two runfolders, e.g. named "runfolder1" and "runfolder2" here for demonstration purposes, type the following on command line

```Bash
$python md5sumscript.py runfolder1 runfolder2
```

5.The outputs should look like this

```
1>runfolder1/bamfile1.bam.md5 is being checked
2>runfolder1/bamfile2.bam.md5 is being checked
3>runfolder1/bamfile3.bam.md5 is being checked
4>runfolder2/bamfile1.bam.md5 is being checked
5>runfolder2/bamfile2.bam.md5 is being checked

6>BACKUP vs ORIGINAL

7>bamfile1.bam.md5 being checked
8>bamfile2.bam.md5 being checked


9>ORIGINAL vs BACKUP

10>bamfile1.bam.md5 being checked
11>bamfile2.bam.md5 being checked
12>bamfile3.bam.md5 being checked

13>md5 matches found 
14>{'backup': {'bamfile2.bam.md5': '...'},
 'original: {'bamfile2.bam.md5': '...'}}

15>md5 mismatches found
16>{'backup': {bamfile1.bam.md5': '1234567890abcdefghijklmnopqrstuv'},
 'original: {'bamfile1.bam.md5': '1234567890abcdefghijklmnopqrs£$%'}}

17>all backup .md5 present in original runfolder
18>md5 in original but not in backup found
19>{'hash present': {},
 'no hash match': {bamfile3.bam.md5: '...'}}

20>estimate of program run time: ###
```

After the program is complete, a summary table of all md5s in the original and backup runfolders is created in your working directory called "md5_table.html". An example of this can be seen here

runfolder1/ and runfolder2/

| md5_filename		| bam_filename(original)	| bam_filename(backup)	| md5_hash(original)			  | md5_hash(backup)				|
|:----------------- |:------------------------- |:--------------------- |:------------------------------- |:------------------------------- |
| bamfile1.bam.md5  | bamfile1.bam 				| bamfile1.bam 			| 1234567890abcdefghijklmnopqrs£$%| 1234567890abcdefghijklmnopqrstuv|
| bamfile2.bam.md5 	| bamfile2.bam 				| bamfile2.bam 			| ...							  | ...							    |
| bamfile3.bam.md5 	| bamfile3.bam 				| NONE					| ...							  | NONE							|

## Output explanation and interpretation

- From line 1 to 5, the output shows the md5 checking process taking place, the md5 hash format (length=32 + alphanumeric), and the bam filenames associated with each md5 are checked to see if they match. Note that md5sum program is invoked to generate the checksum for the bam file associated with the md5 before checking it against the existing one in the bam.md5. The outcome of the checks are stored in the DATE.chk log file in each runfolder.

- From line 6 to 8, the md5 filenames and associated md5 checksums are cross checked between the original and backup runfolder.

- From line 9 to 12, the reverse check is performed, where the md5 filenames and associated md5 checksums are cross checked between the backup and original runfolder.

- From line 13 to 20, all md5 with matching md5 checksum and filename are printed below "md5 matches found", md5s with mismatching checksums are printed below "md5 mismatches found", and md5s that are present alone in either runfolder is displayed under "md5 in original not in backup found" or "md5 in backup not in original found". "hash present" means that md5 checksum present in one runfolder is also present in the other runfolder, but under a different filename, "no hash match" means the md5 checksum in one runfolder is missing and is not found in any md5 files.

- The "md5_table.html" displays the path of the two runfolders at the top of the page, The table is separated into 5 columns. The first column in the table contain all the md5 files that are present in both runfolders, as well as md5 files that are only present in either runfolder (e.g. bamfile4.bam.md5, which is only present in the original runfolder). The second and third column contains the name of the bam file associated with the md5 in the original and backup runfolder respectively. The fourth and fifth column contain the md5 hash associated with each the bam and md5 file in original and backup runfolder respectively.