#!/usr/bin/python
# -*- coding: utf-8 -*-

import imaplib
import email
import datetime
import sys
import time
import os

start_time = time.time()
if len(sys.argv) == 1:
    mail_date = datetime.datetime.now()
else:
    mail_date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

data_date = mail_date - datetime.timedelta(days=1)
filename = "data/%s.xlsx" % data_date.strftime('%Y%m%d')
if os.path.isfile(filename):
    print "Data file already exists, no need to download from mail"
    exit(0)

M = imaplib.IMAP4("email.ele.me")
M.login(os.environ['mail_user'], os.environ['mail_passwd'])
M.select("inbox/dtquery")

print "loop starts in %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
max_num = int(open("max_mail.id").read())
subject = '=?utf-8?q?%s-abn=5Forder=5Fdaily?=' %  mail_date.strftime("%Y-%m-%d")
print "need to find subject:", subject
need_wait = True
while need_wait:
    typ, data = M.search(None, 'ALL')
    nums = map( int, data[0].split() )[::-1]
    nums = filter(lambda x: x > max_num, nums)
    if len(nums) > 1:
        max_num = max(nums)
    for num in nums:
        print "current mail id =", num
	typ, data = M.fetch(num, '(RFC822)')
	mail_string = data[0][1]
	message = email.message_from_string(mail_string)
	print "subject:", message.get("subject")
	if message.get("subject") == subject:
	    # last part is xlsx part
	    print "mail subject matches!"
	    xlsx_part=None
	    for xlsx_part in message.walk():
                pass
	    mail_filename=xlsx_part.get_filename()
	    print mail_filename
	    if mail_filename == "%s-abn_order_daily.xlsx" % mail_date.strftime("%Y-%m-%d"):
	        need_wait = False
	        with open(filename, "wb") as f, open("max_mail.id", "w") as g:
		    f.write(xlsx_part.get_payload(decode=True))
		    print "file %s downloaded sucessfully!" % mail_filename
		    g.write("%s\n" % num)
		    print "write %s to max_mail.id" % num
		break
    time.sleep(1)

M.close()
M.logout()
print "It took %s seconds to run receivemail.py" % (time.time() - start_time)
