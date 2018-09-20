# CBI-5 Programming Project
 - md5sumscript_4.py
 
By Tengyue Zheng
22/02/2018

## Function:

File integrity checker for checking vcf and bam files in a runfolder using Python 2.7.12

To clone Git repository go here: https://github.com/tz2614/

The test bam files are available upon request by email @ tony_zheng35@hotmail.com

## User Requirements:
- check file integrity of the files within the specified runfolder using md5 checksum values.

## User Stories:
- Run md5sumscript_4.py python script by specifying the path of runfolder as argument
```Python
python md5sumscript_4.py /runfolder/
```
The above script includes
a function that checks that there is a .md5 file for every file that do not end in .md5, .err or .chk
```check_md5(check_list)```
a function that creates a list of filepath for checking .md5 (check_list), and list of filepath for creating .md5 (create_list)
```create_md5_list(rf_path)```
a function that create a error log(.err) and check log(.chk) within the specified runfolder
```create_logfiles(rf_path)```
a function that create .md5 for each file in the create_list
```create_md5(create_list)```

- view the results of the check, open the .chk or .err file located within the specified runfolder

```Bash
[user@login01 md5checksum]$ cat testbamfiles/YEAR-MONTH-DAY.chk
[user@login01 md5checksum]$ cat testbamfiles/YEAR-MONTH-DAY.err
```
e.g.
```Bash
[user@login01 md5checksum]$ cat testbamfiles/2018-07-10.chk
~/md5checksum/testbamfiles/bams/tempbam.sorted.rmdup.bam: OK
~/md5checksum/testbamfiles/bams/tempbam.sorted.rmdup.bam.bai: OK
~/md5checksum/testbamfiles/bams/tempbam.sam: OK
~/md5checksum/testbamfiles/bams/tempbam.bam: OK
~/md5checksum/testbamfiles/bams/tempbam.sorted.bam: OK
~/md5checksum/testbamfiles/bams/tempbam.sorted.bam.bai: OK
```

Input: ./md5sumscript_4.py /testbamfiles/bams

Output:

```Bash
checkfilepath created
errorfilepath created
check log ~/md5checksum/testbamfiles/YEAR-MONTH-DAY.chk generated
error log ~/md5checksum/testbamfiles/YEAR-MONTH-DAY.err generated
~md5checksum/testbamfiles/bams/tempbam.sam.md5 checked
~md5checksum/testbamfiles/bams/tempbam.bam.md5 checked
~md5checksum/testbamfiles/bams/tempbam.sorted.bam.md5 checked
~md5checksum/testbamfiles/bams/tempbam.sorted.bam.bai.md5 checked
~md5checksum/testbamfiles/bams/tempbam.sorted.rmdup.bam.md5 checked
~md5checksum/testbamfiles/bams/tempbam.sorted.rmdup.bam.bai.md5 checked
```