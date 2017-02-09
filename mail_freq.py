#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass, imaplib
import email
import datetime
import sys
import time

if len(sys.argv) == 1:
    file_date = datetime.datetime.now()
else:
    file_date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

data_date = file_date - datetime.timedelta(days=1)

M = imaplib.IMAP4("email.ele.me")
M.login("lili.li@ele.me", "^Ada2elm@sh$")
print M.select()

start_time = time.time()
while True:
    typ, data = M.search(None, 'ALL')
    max_mail_id = int(open("max_mail.id").read())
    nums = filter(lambda x: x >= max_mail_id, map(int, data[0].split()))
    with open("max_mail.id", "w") as f:
        f.write("%s\n" % max(nums))
    print "seconds:", time.time() - start_time
    print nums
    time.sleep(0.1)
