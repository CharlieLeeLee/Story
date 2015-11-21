#!"C:\Python27\python.exe"

# CSC210 - log in - 11/08/2015
# Yumeng Liu


# useful for debugging
import cgitb
cgitb.enable()

def noCookiePage():

    print '''
        <html>
        	<head>
        		<title> Story </title>
        		<style type="text/css">
        			h1{
        				text-align:center;
        				color: #337AB7;
        				font-size: 150px;
        				padding-top: 150px;
        				font-family:arial;
        			}
        			body{
        				text-align:center;
        				font-size:50px;
        				color: #337AB7;
        				font-family:arial;
        			}
        			a.button {
            	-webkit-appearance: button;
            	-moz-appearance: button;
            	appearance: button;
        			color: #337AB7;
        			margin:80px;

            	text-decoration:arial;
        			font-size:25px;
        			}

        		</style>
        	</head>
        	<body>
        		<h1> Story </h1>
        		<p> Write your story,dream and life.</p>

        		<A HREF = "CreatAccount.html" class="button">Register</A>
        		<A HREF = "cgi-bin/login.py" class="button">Log in</A>

        	  </form>
          </body>
        </html>
    '''

def CookiePage(username):
        print '<html>'
        print ' <head>'
        print '		<title>'
        print '			Logged In!'
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
