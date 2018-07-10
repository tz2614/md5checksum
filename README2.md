# CBI-5 Programming Project
 - myscript.sh
 - md5sumscript_4.py
 
By Tengyue Zheng
22/02/2018

## Function:

File integrity checker for checking vcf and bam files in a runfolder using Python 2.7.12

To clone Git repository go here: https://github.com/tz2614/

The test bam and vcf files are available upon request by email @ tony_zheng35@hotmail.com

## User Requirements:
- Run the myscript.sh shell script in the original runfolder to create MD5 values for all the bam and vcf files in the runfolder
 (unique valued - 31 characters long), if the .md5 values are not already present. Alternatively, you can run the md5sumscript_4.py to create the .md5 files.

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

The check_md5 function checks the md5 checksum values from the .md5 file against the md5 checksum values generated in situ by running the following command in Bash terminal:

 ```Bash
 md5sum -c X0001234.md5
 ```

Input: ./myscript.sh ./testbamfiles/bams

Output:

```Bash
27e43885cd0f92e0c60b97e19d9499fa  tempbam.bam
05585733ed0049ac9d95f8756a3edc4a  tempbam.sorted.bam
638852e4ef6fa50615a79567326d43a8  tempbam.sorted.bam.bai
4b22dadbcc57009a3f89fb57866d7eaf  tempbam.sorted.rmdup.bam
af1b0691ceb244c6d23d511d33469eeb  tempbam.sorted.rmdup.bam.bai
```
Input: ./md5sumscript_4.py /testbamfiles/bams

Output:

```Bash
