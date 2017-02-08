#!/usr/bin/python
# -*- coding: utf-8 -*- 

# params rpt_date, sender, receiver
## for example 0324 lili.li@ele.me lili.li@ele.me,jiejun.gao@ele.me
import sys
from pprint import pprint

# mail imports
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

rpt_date = sys.argv[1]
me = sys.argv[2]
you = sys.argv[3]

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart()
msg['Subject'] = '异常交易监控日报%s' % rpt_date
msg['From'] = me
msg['To'] = you
pprint(dict(msg))

# html attachment 1
filename=(u"异常交易监控日报%s.html" % rpt_date).encode('utf-8')
html_text = open("output/abn_ord_dly.%s.html" % rpt_date, "rb").read()
html = MIMEApplication(html_text)
html['Content-Disposition'] = "attachment; filename=%s" % filename
msg.attach(html)

# html attachment 2
filename=(u"异常类型细分场景明细%s.html" % rpt_date).encode('utf-8')
html_text2 = open("output/abn_ord_dly_app.%s.html" % rpt_date, "rb").read()
html = MIMEApplication(html_text2)
html['Content-Disposition'] = "attachment; filename=%s" % filename
msg.attach(html)

# mail body
body='''
'''
content = MIMEText(body, 'plain')
msg.attach(content)

s = smtplib.SMTP('email.ele.me')
s.sendmail(me, you.split(","), msg.as_string())
s.quit()
