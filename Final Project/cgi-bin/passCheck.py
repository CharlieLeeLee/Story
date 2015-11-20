#!"C:\Python27\python.exe"

# CSC210 - password check - 11/18/2015
# Charlie Norvell

import cgitb
cgitb.enable()

def printstyle():
    print '<html>'
    print ' <head>'
    print '		<title>'
    print '			Logging In!'
    print '		</title>'
    print '		<style type="text/css">'
    # in Python, use ''' triple quotes ''' to create a multi-line string
    print '''
                            h1 {
                                    font-size: 100px;
                                    font-family: arial;
                                    color: #337AB7;
                            }

                            img {
                                    width: 300px;
                            }

                            h2 {
                                    color: #337AB7;
                                    font-family: arial;
                            }

                            h3 {
                                    font-size: 20px;
                                    font-family: arial;
                                    color: #337AB7;
                    </style>

            </head>
        
    '''

import cgi
form = cgi.FieldStorage()
aname = form['username'].value
pw = form['password'].value

import datetime
from datetime import timedelta
import Cookie
import os
t = str(datetime.datetime.now() + datetime.timedelta(days=1))
cookie = Cookie.SimpleCookie()
import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()
for r in c.execute('select * from accounts where aname=?;',[aname]):
    if r[3] == pw:
        cookie['username'] = aname
        cookie['username']['expires'] = t
        print "Content-type: text/html"
        print cookie
        print
        print '<html>'
        print '<head>'
        print '    <meta charset="UTF-8">'
        print '    <meta http-equiv="refresh" content="1;url=profile.py?aname=' + aname + '">'
        print '    <script type="text/javascript">'
        print '        window.location.href = "profile.py?aname=' + aname + '"'
        print '    </script>'
        print '    <title>Page Redirection</title>'
        print '</head>'
        print '<body>'
        print '        If you are not redirected automatically, follow the <a href="profile.py?aname=' + aname + '">link to Home page</a>'
        print '</body>'
        print '</html>'
        conn.close()
        
    else:
        print "Content-type: text/html"
        print
        printstyle()
        print '<body>'
        print '<p>Incorrect password</p>'
        print '</body>'
        print '</html>'
        conn.close()
    
conn.close()
print "Content-type: text/html"
print
print '<html>'
printstyle()
print '<h2>User not found</h2>'
print '<p>The username you are trying to use does not exist.</p>'
print '<p><a href="../CreatAccount.html">Click here to create a new account</a></p>'
print '</body>'
print '</html>'
