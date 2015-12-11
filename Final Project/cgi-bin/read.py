#!"C:\Python27\python.exe"

# Yumeng Liu


# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

import Cookie
import os
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

aname = cookie['username'].value

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}

for r in c.execute('select * from accounts where aname=?;', [aname]):
        firstname = r[1]
        lastname = r[2]
        writingtalent = r[5]
	profile = r[4]

	data['firstname'] = firstname
	data['lastname'] = lastname
	data['writingtalent'] = writingtalent
        data['profile'] = profile
	print json.dumps(data)

conn.close()
