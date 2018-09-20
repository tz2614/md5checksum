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

- Before running the program, please read the following instructions:

1. Navigate to your working directory and create an empty folder called "bam_check". 

2. If popssible create a virutal environment, so that you can control the library package available for use. To run the script without testing, standalone python 2.7.5 should be sufficient. The program have not been tested in python 3, but if you wish to, eel free to change the print statements in yours scripts after you have cloned the repository in your local workng directory to test the script in python3.

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

c) activate the environment
```Bash
$ source bam_check/bin/activate
```

d) check you have git installed
```Bash
$ git --version
git version 1.8.3.1
```

2. First, clone the repository using git
```Bash
git clone https://github.com/tz2614/md5checksum
or 
git clone https://git.ctrulab.uk/zhengt/md5checksum 
```

- This should create directory called "md5checksum" in your bam_check directory.
- check to make sure the main script called "md5sumscript.py" is present
- If you know where you bam files are located, then try to use the full path to the directory if possible.
- If you only have one runfolder, then I would suggest running md5sumscript_for1runfolder.py instead.

3. Navigate to the runfolder md5checksum and execute the program for two runfolders, e.g. named "runfolder1" and "runfolder2" here for demonstration purposes, type following on command line

```Bash
$python md5sumscript.py runfolder1 runfolder2
```

4.The outputs should look like this

```Bash
1>runfolder1/bamfile1.bam.md5 present
...
2>runfolder1/bamfile2.bam.md5 missing
3>creating a new md5 file: runfolder1/bamfile2.bam.md5
4>new md5 file runfolder1/bamfile2.bam.md5 generated
5>list of new md5s generated:["runfolder1/bamfile2.bam.md5"...]
...
6>runfolder2/bamfile1.bam.md5 present
...
7>list of new md5s generated:[...]
...
8>checkfilepath created
9>check log runfolder1/YYYY-DD-MM.chk generated
10>checkfilepath created
11>check log runfolder2/YYYY-DD-MM.chk generated

12>runfolder1/bamfile1.bam.md5 is being checked
13>OK, bamfile1.bam.md5: 1234567890abcdefghijklmnop have 32 characters and contain only letters or numbers
14>OK, bamfile1.bam match bamfile1.bam in runfolder1/bamfile1.bam.md5
15>cd runfolder1
16>md5sum -c bamfile1.bam.md5
17>bamfile1.bam: OK
18>bamfile1.bam.md5 checked
...

19>runfolder2/bamfile1.bam.md5 is being checked
20>ERROR, bamfile1.bam.md5: £$%1234567890abcdefghijklmn DO NOT have 32 characters or contain non-alphanumeric characters.
21>ERROR, bamfile1.bam DO NOT match bamfile5.bam in runfolder2/bamfile1.bam.md5
21>bamfile1.bam.md5 checked
...

22>{'archive': {'bamfile1.bam.md5' : '1234567890abcdefghijklmnop',
			...},
23>{'storage': {'bamfile1.bam.md5' : '...',
			...}}

24>BACKUP vs ORIGINAL

25>bamfile1.bam.md5 being checked
26>OK, bamfile1.bam.md5 present in backup and original runfolder
27>ERROR, 1234567890abcdefghijklmnop and £$%1234567890abcdefghijklmn in bamfile1.bam.md5 DO NOT MATCH

28>bamfile2.bam.md5 being checked
29>OK, bamfile2.bam.md5 present in backup and original runfolder
30>OK, bamfile2.bam.md5 has matching hash
...

31>bamfile3.bam.md5 being checked
32>ERROR, bamfile3.bam.md5 not present in original runfolder
...

33>ORIGINAL vs BACKUP

34>bamfile1.bam.md5 being checked
35>OK, bamfile1.bam.md5 present in backup and original runfolder
36>ERROR, £$%1234567890abcdefghijklmn and 1234567890abcdefghijklmnop in bamfile1.bam.md5 DO NOT MATCH

37>bamfile2.bam.md5 being checked
38>OK, bamfile2.bam.md5 present in original and backup runfolder
39>OK, bamfile2.bam.md5 has matching hash

40>bamfile4.bam.md5 being checked
41>ERROR, bamfile3.bam.md5 not present in backup runfolder
...

42>md5 matches found 
43>{'backup': {'bamfile2.bam.md5': '...'},
 'original: {'bamfile2.bam.md5': '...'}}

44>md5 mismatches found
45>{'backup': {bamfile1.bam.md5': '1234567890abcdefghijklmnop'},
 'original: {'bamfile1.bam.md5': '£$%1234567890abcdefghijklmn'}}

46>all backup .md5 present in original runfolder
47>md5 in original but not in backup found
48>{'hash present': {},
 'no hash match': {bamfile3.bam.md5: '...'}}

49>estimate of program run time: ###
 ```

## Output explanation and interpretation

- From line 1 to 7, the output shows which md5 files are present, which md5 files are missing, and which md5 files have been generated.

- From line 8 to 11, the output shows the log files in the form of YYYY-DD-MM.chk that have beend generated ready to receive logs from the md5 check

- From line 12 to 21, the output shows the md5 checking process taking place, the md5 hash format (length=32 + alphanumeric), and the bam filenames associated with each md5 are checked to see if they match. Note that md5sum program is invoked to generate the md5 checksum for the bam file associated with the md5 before checking it against the existing one. 

- From line 22 to 23, the md5 filenames and associated hash are added to a dictionary and displayed on the terminal

- From line 24 to 32, the md5 filenames and associated md5 checksums are cross checked by iterating through the list of filenames in the original dictionary.

- From line 33 to 41, the md5 filenames and associated md5 checksums are cross checked by iterating through the list of filenames in the backup dictionary.

- From line 42 to 48, all md5 with matching md5 checksum and filename are printed below "md5 matches found", md5s with mismatching checksums are printed below "md5 mismatches found". And md5s that are present alone in either runfolder is displayed under "md5 in original not in backup found" or "md5 in backup not in original found". "hash present" means that md5 checksum present in one runfolder is also present in the other runfolder, but under a different filename "no hash match" means the md5 checksum in one runfolder is missing and is not found in any md5 files.