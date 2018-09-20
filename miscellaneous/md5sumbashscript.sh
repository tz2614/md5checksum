#!/bin/bash
# checks files and clones has the same file integrity as each other
# Tengyue 21/2/2018

# Do we already have a check file in the runfolder?

checkfile=`date +%F`
errorfile=`date +%F`_e
md5file=`./hash.md5`
backupfolder=`data/projects/zhengt/backup/`

if [ $# != 1 ]
then
  echo 'provide single argument which is the directory to backup'
  exit
fi

if [ ! -d $backupfolder ]
then
  echo 'The directory given does not exist'
  exit
fi

if  [ ! -f $md5file ]
then
  echo 'The md5file do not exist, would you like to add one?'
  read answer
  if [ $answer != 'y' ]
  then
    md5sum *.bam /vcfs/*.vcf *.vcf > $md5file
    cp $md5file $backupfolder
  else
    echo 'This folder has already been checked today'
  exit
fi

md5sum -c $backupfolder/$md5file > $4/$checkfile
cat $4/checkfile
md5sum -c $backupfolder/$md5file 2> $4/$errorfile
cat $4/errorfile


# Is the md5sum checksum the same between copy and original file?

if [ cut -f 2 -d ' ' checkfile | if $1==OK ]
    echo file integrity intact >> $1_$checkfile
fi
else
    echo file integrity compromised >> $1_$checkfile
done

