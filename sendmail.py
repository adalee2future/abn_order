#!/usr/bin/python
# -*- coding: utf-8 -*- 

# params rpt_date, sender, receiver
## for example 0324 lili.li@ele.me lili.li@ele.me,jiejun.gao@ele.me
import sys
import os
from pprint import pprint
import urllib

# mail imports
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

rpt_date = sys.argv[1]
rpt_date_md = rpt_date[4:]
me = sys.argv[2]
you = sys.argv[3]

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart()
msg['Subject'] = '异常交易监控日报%s' % rpt_date_md
msg['From'] = me
msg['To'] = you
pprint(dict(msg))

# html attachment 1
filename=(u"异常交易监控日报%s.html" % rpt_date_md).encode('utf-8')
html_text = open("output/abn_ord_dly.%s.html" % rpt_date, "rb").read()
html = MIMEApplication(html_text)
html['Content-Disposition'] = "attachment; filename=%s" % Header(filename, 'UTF-8')
msg.attach(html)

# html attachment 2
filename=(u"异常类型细分场景明细%s.html" % rpt_date_md).encode('utf-8')
html_text2 = open("output/abn_ord_dly_app.%s.html" % rpt_date, "rb").read()
html = MIMEApplication(html_text2, 'uft-8')
html['Content-Disposition'] = "attachment; filename=%s" % Header(filename, 'UTF-8')
msg.attach(html)

# mail body
body = open("output/abn_ord_dly_smy.%s.html" % rpt_date, "rb").read()
content = MIMEText(body, 'html', 'utf-8')
msg.attach(content)

s = smtplib.SMTP('email.ele.me')
# 登录的话收件人可以是外网，不登录的话可以是公司内部任意发件人
s.login(os.environ['mail_user'], os.environ['mail_passwd']) #登录
s.sendmail(me, you.split(","), msg.as_string())
s.quit()
