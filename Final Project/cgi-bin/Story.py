#!"C:\Python27\python.exe"

# CSC210 - log in - 11/08/2015
# Yumeng Liu


# useful for debugging
import cgitb
cgitb.enable()

def noCookiePage():

    print '<html>'
    print ' <head>'
    print '		<title>'
    print '			Story'
    print '		</title>'
    print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
    # in Python, use ''' triple quotes ''' to create a multi-line string
    print '''
    	</head>
    	<body>
    '''
    print '<meta http-equiv="refresh"'
    print 'content="0; url=../Story.html">'

def CookiePage(username):
        print '<html>'
        print ' <head>'
        print '    <meta charset="UTF-8">'
        print '    <meta http-equiv="refresh" content="1;url=login.py">'
        print '    <script type="text/javascript">'
        print '        window.location.href = "profile.py?aname=' + username+'"'
        print '    </script>'
        print '    <title>Page Redirection</title>'
        print '		<title>'
        print '			Logged In!'
        print '		</title>'
        print '         <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
        print ' </head>'
        print '<body>'
        print'''
        		<header>
        			<ul style="position:fixed;">
        				<li><a href="Story.py">Story</a></li>
        				<li><a name="about" href="../Story.html#about">About</a></li>
        				<ul style="float:right;list-style-type:none;">
        '''
        print '					<li><a href="profile.py?aname=' + username + '">' + username + '</a></li>'
        print'''		</ul>
        			</ul>
        		</header>
        '''
        print '<h2>Hello ' + username +'</h2>'
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
    noCookiePage()

else:
    cookie = Cookie.SimpleCookie(stored_cookie_string)
    # if it's an appropriate cookie, use it
    if 'username' in cookie:
            aname = cookie['username'].value

            print "Content-type: text/html"
            print
            CookiePage(aname)

    # if cookie is useless
    else:
            print "Content-type: text/html"
            print # don't forget the extra newline!
            noCookiePage()

print '	</body>'
print '</html>'
