#!"C:\Python27\python.exe"

# CSC210 - Delete 12/3/2015
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


import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


def notLoggedInPage():
    print '<html>'
    print ' <head>'
    print '		<title>'
    print '			Not Logged In'
    print '		</title>'
    print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css">'
    print ' </head>'
    print '<body>'
    print '''
    <header>
        <ul style="position:fixed;">
            <li><a href="Story.py">Story</a></li>
            <li><a name="about" href="../Story.html#about">About</a></li>
            <ul style="float:right;list-style-type:none;">
                 <li><a href="../CreatAccount.html">Sign Up</a></li>
                 <li><a href="login.py">Sign In</a></li>
            </ul>
        </ul>
    </header>
    '''
    print ' <h2>Not Logged In</h2>'

def loggedInPage():
    print '<html>'
    print ' <head>'
    print '		<title>'
    print '			Account Deleted'
    print '		</title>'
    print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css">'
    print ' </head>'
    print '<body>'
    print '''
    <header>
        <ul style="position:fixed;">
            <li><a href="Story.py">Story</a></li>
            <li><a name="about" href="../Story.html#about">About</a></li>
            <ul style="float:right;list-style-type:none;">
                 <li><a href="../CreatAccount.html">Sign Up</a></li>
                 <li><a href="login.py">Sign In</a></li>
            </ul>
        </ul>
    </header>
    '''
    print ' <h2>Account Deleted</h2>'

import datetime
expires = datetime.datetime.utcnow() - datetime.timedelta(days=30)

# if not logged in, show login screen.
stored_cookie_string = os.environ.get('HTTP_COOKIE')

if not stored_cookie_string:
        print "Content-type: text/html"
        print
        notLoggedInPage()

else:
        cookie = Cookie.SimpleCookie(stored_cookie_string)
        # if it's an appropriate cookie, use it
        if 'username' in cookie:
                cookie['username']['expires']=expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
                c.execute('delete from accounts where aname=?;', (aname,))
                print "Content-type: text/html"
                print cookie
                print
                loggedInPage()

        # if cookie is useless
        else:
                print "Content-type: text/html"
                print # don't forget the extra newline!
                notLoggedInPage()

print '	</body>'
print '</html>'

conn.commit()

conn.close()
