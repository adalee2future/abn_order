#/bin/ksh -eu

# sender and receiver can be any mail in host ele.me
from=lili.li@ele.me
to=fei.ren@ele.me,jiejun.gao@ele.me,ruiqing.zhang@ele.me,fanjing.lv@ele.me,diting.liu@ele.me,lili.li@ele.me  #delimiter "," if multiple recipients
#to=lili.li@ele.me

if [ $# -eq 0 ];
  then rpt_date=`date -v -1d '+%m%d'` # This could be only run in mac
else
  rpt_date=$1
fi

echo "rpt_date"
echo $rpt_date

if [ ! -f data/$rpt_date-all.xlsx ]
then 
  echo "Error, data file not exists!"
  exit -1
fi

# generate report using R
R -e "rmarkdown::render('abn_order_daily2.Rmd', output_format='html_document')"
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

