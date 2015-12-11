#!"C:\Python27\python.exe"

# CSC210 - Update Account - 11/08/2015
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
picture = form['profile'].value


import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}


c.execute("""
        UPDATE accounts
        SET fname=?, lname=?, image=?, writing=?
        WHERE aname=?
        """, (firstname, lastname, picture, talent, aname))
conn.commit()

conn.close()
