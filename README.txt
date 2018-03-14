# BIOL68400 Programming Project
# myscript.sh
# By Tengyue Zheng
# 22 Feb 2018

Function:

md5sum file integreity checker for checking vcf and bam files in a runfolder using Python 2.7.12

To clone Git repository go here: https://github.com/tz2614/

The test bam and vcf files are available upon request by email @ tony_zheng35@hotmail.com

User Requirements:
- Run the shell/python script in the original runfolder to create MD5 values for all the bam and vcf files in the runfolder
 (unique valued - 31 characters long)

User Stories:
- run python script by specifying the path of runfolder and path of the md5file as arguments
- Input logic tests
- Parse the md5 checksum values and filenames to a .md5 file and cross check the md5 checksum values in the backup folder by running the following command in the shell script:

# md5sum -c hash.md5

Input: ./myscript.sh /data/gemini/180222_180223

Output:

27e43885cd0f92e0c60b97e19d9499fa  tempbam.bam
05585733ed0049ac9d95f8756a3edc4a  tempbam.sorted.bam
638852e4ef6fa50615a79567326d43a8  tempbam.sorted.bam.bai
4b22dadbcc57009a3f89fb57866d7eaf  tempbam.sorted.rmdup.bam
af1b0691ceb244c6d23d511d33469eeb  tempbam.sorted.rmdup.bam.bai
