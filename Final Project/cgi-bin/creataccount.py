#!"C:\Python27\python.exe"

# CSC210 - creat account - 11/08/2015
# Yumeng Liu

# To run, start AMPSS and visit URLs like the following to insert new
# entries into the database, then check your database's contents using
# lecture4-query-database.py
#
# http://localhost/cgi-bin/lecture4.py?my_name=Joe&my_age=32&my_image=../cat.jpg
# http://localhost/cgi-bin/lecture4.py?my_name=Donna&my_age=37&my_image=../dog.jpg

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

fname = form['firstname'].value
lname = form['lastname'].value
aname = form['accountname'].value
pw = form['password'].value
writing = form['writingtalent'].value
image = form['profile'].value


# insert new user data into the database
import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('insert into accounts values (?, ?, ?, ?, ?, ?)', (aname, fname, lname, pw, image, writing))
conn.commit()

# creat a cookie
import Cookie
import os

import datetime


cookie = Cookie.SimpleCookie()
cookie['username'] = aname
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) # expires in 30 days
cookie['username']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
#cookie['username']['expires'] = time.strftime("%a, %d-%b-%Y %T GMT", t)

# print the http header
print "Content-Type: text/html"
print cookie
print # don't forget the extra newline

print '<html>'
print ' <head>'
print '		<title>'
print '			Account Page'
print '		</title>'
print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
# in Python, use ''' triple quotes ''' to create a multi-line string
print '''
	</head>
	<body>
'''
print '<meta http-equiv="refresh"'
print 'content="0; url=profile.py?aname='+aname+'">'


conn.close()

print '	</body>'
print '</html>'
