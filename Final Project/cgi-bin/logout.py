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
        print '<div id="signin">'
        print '''
        <header>
			<ul style="position:fixed;">
				<li><a href="Story.py">Story</a></li>
				<li><a name="about" href="../Story.html#about">About</a></li>
				<ul style="float:right;list-style-type:none;">
					<li><a href="../CreatAccount.html">Sign Up</a></li>
					<li><a class="active" href="cgi-bin/login.py">Sign in</a></li>
				</ul>
			</ul>
		</header>
        '''
        print'<h2>Please Sign In</h2>'
        print'<form method="post" action="passCheck.py">'
        print '''
        <p>
           <label for="username"/>
           <input id="username" name="username" type="text" required="required" placeholder="Account Name">
        </p>
        <p>
           <label for="password"/>
           <input id="password" name="password" type="password" required="required" placeholder="Password">
        </p>

        '''
        print'<button class="button" type="submit">Sign In</button>'
        print'</form>'
        print'</div>'
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
        print'''
        		<header>
        			<ul style="position:fixed;">
        				<li><a href="Story.html">Story</a></li>
        				<li><a name="about" href="Story.html#about">About</a></li>
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
                print "Content-type: text/html"
                print cookie
                print
                notLoggedInPage()

        # if cookie is useless
        else:
                print "Content-type: text/html"
                print # don't forget the extra newline!
                notLoggedInPage()

print '	</body>'
print '</html>'
