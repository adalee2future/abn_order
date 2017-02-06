#/bin/ksh -eu

# sender and receiver can be any mail in host ele.me
from=lili.li@ele.me
to=lili.li@ele.me  #delimiter "," if multiple recipients

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
	

# generate Rmd file
sed "s/DATE_MMDD/$rpt_date/g" template.Rmd > 异常交易监控日报$rpt_date.Rmd
# generate report using R
R -e "rmarkdown::render('异常交易监控日报$rpt_date.Rmd', output_format='html_document')"

# send mail using python
./sendmail.py $rpt_date $from $to

mv 异常交易监控日报$rpt_date.* output/
