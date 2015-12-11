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
    print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
    print ' </head>'
import cgi
form = cgi.FieldStorage()
aname = form['username'].value
pw = form['password'].value

import datetime
from datetime import timedelta

import Cookie
import os
#set up for 1 day to make the cookie expire
#t = str(datetime.datetime.now() + datetime.timedelta(days=1))
#t = str(datetime.datetime.now() + datetime.timedelta(days=1))
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) # expires in 30 days
import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()
baduser = True;
for r in c.execute('select * from accounts where aname=?;',[aname]):
    baduser = False;
    if r[3] == pw:
        cookie = Cookie.SimpleCookie()
        cookie['username'] = aname
        cookie['username']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")

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
        print '''
        <header>
            <ul style="position:fixed;">
                <li><a href="Story.py">Story</a></li>
                <li><a name="about" href="../Story.html#about">About</a></li>
                <ul style="float:right;list-style-type:none;">
                     <li><a href="CreatAccount.html">Sign Up</a></li>
					 <li><a href="cgi-bin/login.py">Sign in</a></li>
                </ul>
            </ul>
        </header>
        '''
        print '     If you are not redirected automatically, follow the <a href="profile.py?aname=' + aname + '">link to Home page</a>'
        print '</body>'
        print '</html>'

    else:
        print "Content-type: text/html"
        print
        printstyle()
        print '<body>'
        print '''
        <header>
            <ul style="position:fixed;">
                <li><a href="Story.py">Story</a></li>
                <li><a name="about" href="../Story.html#about">About</a></li>
                <ul style="float:right;list-style-type:none;">
                     <li><a href="../CreatAccount.html">Sign Up</a></li>
					 <li><a href="login.py">Sign in</a></li>
                </ul>
            </ul>
        </header>
        '''
        print '<h2>Incorrect password</h2>'
        print '<p style="text-align:center;">Please click SIGN IN to try again, or SIGN UP to create a new account.</p>'
        print '</body>'
        print '</html>'
if (baduser):
    print "Content-type: text/html"
    print
    print '<html>'
    printstyle()
    print '<body>'
    print '''
    <header>
        <ul style="position:fixed;">
            <li><a href="Story.py">Story</a></li>
            <li><a name="about" href="../Story.html#about">About</a></li>
            <ul style="float:right;list-style-type:none;">
                 <li><a href="../CreatAccount.html">Sign Up</a></li>
                 <li><a href="login.py">Sign in</a></li>
            </ul>
        </ul>
    </header>
    '''
    print '<h2>User not found</h2>'
    print '<p style="text-align:center;">Please click SIGN UP to create a new account.</p>'
    print '</body>'
    print '</html>'

conn.close()
