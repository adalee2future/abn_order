#/bin/ksh -eu

# sender and receiver can be any mail in host ele.me
from=lili.li@ele.me
#to=fei.ren@ele.me,jiejun.gao@ele.me,ruiqing.zhang@ele.me,fanjing.lv@ele.me,diting.liu@ele.me,minqiu.wang@ele.me,lili.li@ele.me  #delimiter "," if multiple recipients
to=lili.li@ele.me

if [ $# -eq 0 ];
  #then rpt_date=`date -v -1d '+%m%d'` # This could be only run in mac
  then rpt_date=0206
else
  rpt_date=$1
fi

echo "rpt_date"
echo $rpt_date

# send mail using python
./sendmail.py $rpt_date $from $to
