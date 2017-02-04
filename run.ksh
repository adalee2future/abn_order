#/bin/ksh -eu
rpt_date=0203
sed "s/DATE_MMDD/$rpt_date/g" template.Rmd > 异常交易监控日报$rpt_date.Rmd
R -e "rmarkdown::render('异常交易监控日报$rpt_date.Rmd', output_format='html_document')"
HTML_FILE_CONTENT=`cat 异常交易监控日报$rpt_date.html`

sendmail -t <<EOT
From: adalee.is.here@gmail.com
To: fei.ren@ele.me,jiejun.gao@ele.me,lili.li@ele.me
Subject: 异常交易监控日报$rpt_date 
MIME-Version: 1.0
Content-Type: multipart/related;boundary="XYZ"

--XYZ
Content-Type: text/html

<html>
</html>

--XYZ
Content-Type: text/html
Content-Disposition: attachment; filename*=UTF-8''%E5%BC%82%E5%B8%B8%E4%BA%A4%E6%98%93%E7%9B%91%E6%8E%A7%E6%97%A5%E6%8A%A5$rpt_date.html

$HTML_FILE_CONTENT
--XYZ--
EOT
echo "email sent! please check"
mv 异常交易监控日报$rpt_date.* output/
