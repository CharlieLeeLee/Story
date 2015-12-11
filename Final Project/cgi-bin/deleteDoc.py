#!"C:\Python27\python.exe"

# CSC210 - Delete Document 12/11/2015
# Charlie Norvell


# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()
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
        DELETE from documents where address=?
        """, (url,))
data['url']=url
print json.dumps(data)
conn.commit()

conn.close()
