#!/usr/bin/python
# -*- coding: utf-8 -*- 

# params rpt_date, sender, receiver
## for example 0324 lili.li@ele.me lili.li@ele.me,jiejun.gao@ele.me
import sys

# mail imports
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

rpt_date = sys.argv[1]
me = sys.argv[2]
you = sys.argv[3]
print(sys.argv)
print(rpt_date)

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart()
msg['Subject'] = '异常交易监控日报%s' % rpt_date
msg['From'] = me
msg['To'] = you

html_text = open("%s.html" % msg['Subject'], "rb").read()
html = MIMEApplication(html_text)
html['Content-Disposition'] = "attachment; filename*=''%E5%BC%82%E5%B8%B8%E4%BA%A4%E6%98%93%E7%9B%91%E6%8E%A7%E6%97%A5%E6%8A%A5" + rpt_date + ".html"

msg.attach(html)

s = smtplib.SMTP('email.ele.me')
s.sendmail(me, you, msg.as_string())
s.quit()
