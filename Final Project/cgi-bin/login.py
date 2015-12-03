#!"C:\Python27\python.exe"

# CSC210 - log in - 11/08/2015
# Charlie Norvell


# useful for debugging
import cgitb
cgitb.enable()

def notLoggedInPage():

        print '<html>'
        print ' <head>'
        print '		<title>'
        print '			Logging In...'
        print '		</title>'
        # in Python, use ''' triple quotes ''' to create a multi-line string
        print '''
                <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>               

                </head>
        '''
        print '<body>'
        print'<h2>You are not yet logged in.</h2>'
        print'<form method="post" action="passCheck.py">'
        print'Username:'
        print'<input name="username" type=text size="30"/>'
        print'<br><br>'
        print'Password:'
        print'<input name="password" type=text size="30"/>'
        print'<input type="submit"/>'
        print'</form>'
        print'</body></html>'

def loggedInPage(username):
        print '<html>'
        print ' <head>'
        print '		<title>'
        print '			Logged In!'
        print '		</title>'
        print '         <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
        print ' </head>'
        print '<body>'
        print '<h1>Hello ' + username +'</h1>'
        print '<a href="profile.py?aname=' + username + '">Your Profile</a>'
        print '</body></html>'

import Cookie
import os

import cgi
form = cgi.FieldStorage()

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
                aname = cookie['username'].value

                print "Content-type: text/html"
                print
                loggedInPage(aname)

        # if cookie is useless
        else:
                print "Content-type: text/html"
                print # don't forget the extra newline!
                notLoggedInPage()

print '	</body>'
print '</html>'
