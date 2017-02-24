#!/bin/ksh -eu
## ./run.ksh YYYYMMDD

echo "shell started at `date +'%Y-%m-%d %H:%M:%S'`"
START=$(date +%s)
. ~/.profile
cd ~/projects/abn_order2
export PATH=/usr/local/bin:$PATH

# sender and receiver can be any mail in host ele.me
from=lili.li@ele.me
to=fei.ren@ele.me,jiejun.gao@ele.me,lili.li@ele.me,ruiqing.zhang@ele.me,fanjing.lv@ele.me,diting.liu@ele.me,minqiu.wang@ele.me,xiangfei.ye@ele.me,yue.mao@ele.me  #delimiter "," if multiple recipients
#to=lili.li@ele.me,jiejun.gao@ele.me
#to=lili.li@ele.me


if [ $# -eq 0 ];
  then rpt_date=`date -v -1d '+%Y%m%d'` # This could be only run in mac
else
  rpt_date=$1
fi

echo "rpt_date: $rpt_date"

# fetch data from email
mail_date=`date -j -v +1d -f "%Y%m%d" $rpt_date +%Y%m%d`
echo "mail_date: $mail_date"
./receivemail.py $mail_date

if [ ! -f data/$rpt_date.xlsx ]
then 
  echo "Error, data file not exists!"
  exit -1
fi

# generate report using R
R --no-save << EOT
rmarkdown::render('abn_order_daily2.Rmd',
                  output_format='html_document',
		  output_file='abn_ord_dly.$rpt_date.html',
		  params=list(rpt_date="$rpt_date")
)

rmarkdown::render('abn_ord_dly_app.Rmd',
                  output_format='html_document',
		  output_file='abn_ord_dly_app.$rpt_date.html',
		  params=list(rpt_date="$rpt_date")
)

EOT

mv abn_ord_dly*.$rpt_date.html output/

# send mail using python
./sendmail.py $rpt_date $from $to

echo "shell completed at `date +'%Y-%m-%d %H:%M:%S'`"
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds to run run.ksh"
echo 
