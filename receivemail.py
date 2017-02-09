#!/usr/bin/python
# -*- coding: utf-8 -*-

import imaplib
import email
import datetime
import sys
import time
import os

if len(sys.argv) == 1:
    mail_date = datetime.datetime.now()
else:
    mail_date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

data_date = mail_date - datetime.timedelta(days=1)

M = imaplib.IMAP4("email.ele.me")
M.login(os.environ['mail_user'], os.environ['mail_passwd'])
M.select()

print "loop starts in %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
start_time = time.time()
need_wait = True
while need_wait:
        
    typ, data = M.search(None, 'ALL')
    max_mail_id = int(open("max_mail.id").read())
    nums = filter(lambda x: x > max_mail_id, map(int, data[0].split()))
    subject = '=?utf-8?q?%s-all?=' %  mail_date.strftime("%Y-%m-%d")
    print "need to find subject:", subject
	    
    for num in nums:
        print "current mail id =", num
	typ, data = M.fetch(num, '(RFC822)')
	mail_string = data[0][1]
	message = email.message_from_string(mail_string)
	if message.get("subject") == subject:
	    # last part is xlsx part
	    print "mail subject matches!"
	    xlsx_part=None
	    for xlsx_part in message.walk():
                pass
	    mail_filename=xlsx_part.get_filename()
	    if mail_filename == "%s-all.xlsx" % mail_date.strftime("%Y-%m-%d"):
	        need_wait = False
		filename = "data/%s.xlsx" % data_date.strftime('%Y%m%d')
	        with open(filename, "wb") as f:
		    f.write(xlsx_part.get_payload(decode=True))
		    print "file %s downloaded sucessfully!" % mail_filename
		break

    with open("max_mail.id", "w") as f:
        f.write("%s\n" % num)
    time.sleep(0.1)
print "Seconds took:", time.time() - start_time
M.close()
M.logout()
