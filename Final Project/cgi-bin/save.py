#!"C:\Python27\python.exe"

# CSC210 - Save Document - 12/1/2015
# Charlie Norvell


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
title = form['dname'].value
url = form['url'].value


import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}


c.execute("""
        INSERT into documents values(?, ?, ?)
        """, (title, url, aname))
conn.commit()

conn.close()
