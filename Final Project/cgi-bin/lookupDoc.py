#!"C:\Python27\python.exe"

# Look up A Story
# Yumeng Liu

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

story_title = form['story_title'].value

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}

for r in c.execute('select * from documents where title=?;', [story_title]):
	title = r[0]
	address = r[1]
	description = r[3]

	#print name + ' ' + str(age) + ' ' + image

	data['title'] = title
	data['address'] = address
	data['description'] = description
	print json.dumps(data)

conn.close()
