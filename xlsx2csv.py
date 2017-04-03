#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
import xlrd
import datetime
def csv_from_excel(xlsx_filename, sheet_name, csv_filename):
    xlsx_file = xlrd.open_workbook(xlsx_filename, encoding_override="utf-8")
    sheet = xlsx_file.sheet_by_name(sheet_name)
    csv_file = open(csv_filename, 'w')
    for rownum in xrange(sheet.nrows):
	row_values = sheet.row_values(rownum)
	if rownum > 0:
	    row_values[4] = int(row_values[4])
	row_values = map(unicode, row_values)
	line = '%s\n' % (','.join(row_values))
	csv_file.write(line.encode('utf8'))
    csv_file.close()

if len(sys.argv) == 1:
    mail_date = datetime.datetime.now()
else:
    mail_date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

data_date = mail_date - datetime.timedelta(days=1)
xlsx_filename = "data/%s.xlsx" % data_date.strftime('%Y%m%d')
print "xlsx filename:", xlsx_filename
sheet_name = 'Sheet0'
csv_filename = "data/%s.csv" % data_date.strftime('%Y%m%d')
print "csv filename:", csv_filename
csv_from_excel(xlsx_filename, sheet_name, csv_filename)
