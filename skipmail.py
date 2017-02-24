#!/usr/bin/python
# -*- coding: utf-8 -*-

import imaplib
import os

def login_mail():
    M = imaplib.IMAP4("email.ele.me")
    login_status, _ = M.login(os.environ['mail_user'], os.environ['mail_passwd'])
    M.select()
    return M

M = login_mail()
max_num = int(open("max_mail.id").read())
typ, data = M.search(None, 'ALL')
nums = map( int, data[0].split() )
with open("max_mail.id", 'w') as f:
    line = "%s\n" % max(nums)
    print line
    f.write(line)

M.close()
M.logout()
