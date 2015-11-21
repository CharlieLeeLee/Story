#!"C:\Python27\python.exe"

# CSC210 - log in - 11/08/2015
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
firstname = form['first_name'].value
lastname = form['last_name'].value
talent = form['writing_talent'].value
picture = form['profile_picture'].value


import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}

for r in c.execute('select * from accounts where aname=?;', [aname]):
##        r[1] = firstname
##        r[2] = lastname
##        r[5] = talent
##        r[4] = picture

        #print name + ' ' + str(age) + ' ' + image

        data['myName'] = firstname + " " +lastname
        data['myTalent'] = talent
        data['myImage'] = picture
        print json.dumps(data)

conn.close()
