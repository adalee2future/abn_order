#!/bin/ksh -eu
## ./run.ksh YYYYMMDD

echo "shell started at `date +'%Y-%m-%d %H:%M:%S'`"
START=$(date +%s)
. ~/.profile
cd ~/projects/abn_order2
export PATH=/usr/local/bin:$PATH

# sender and receiver can be any mail in host ele.me if not login
export from=$mail_user
if [ -z ${to+x} ]
  then export to=$mail_user
fi


# set up rpt_date
if [ $# -eq 0 ];
  then export rpt_date=`date -v -1d '+%Y%m%d'` # This could be only run in mac
else
  export rpt_date=$1
fi

echo "rpt_date: $rpt_date"

# fetch data from email
export mail_date=`date -j -v +1d -f "%Y%m%d" $rpt_date +%Y%m%d`
echo "mail_date: $mail_date"
./receivemail.py $mail_date

# check if file exists
if [ ! -f data/$rpt_date.xlsx ]
then 
  echo "Error, data file not exists!"
  exit -1
fi

# convert xlsx to csv
./xlsx2csv.py $mail_date

# generate report using R
./generate_report.ksh

# send mail using python
./sendmail.py $rpt_date $from $to

echo "shell completed at `date +'%Y-%m-%d %H:%M:%S'`"
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds to run run.ksh"
echo 
