#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from pprint import pprint
import os

# mail imports
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_filename = sys.argv[1]
me = os.environ['mail_user']
you=me

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart()
msg['Subject'] = 'abn_order: %s' % log_filename
msg['From'] = me
msg['To'] = you
pprint(dict(msg))


# mail body
body = open(log_filename).read()
content = MIMEText(body, 'plain')
msg.attach(content)

s = smtplib.SMTP('email.ele.me')
s.sendmail(me, you.split(","), msg.as_string())
s.quit()
