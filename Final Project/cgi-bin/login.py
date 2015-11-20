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
        print'<p>You are not yet logged in.</p>'
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

# if not logged in, show login screen.
stored_cookie_string = os.environ.get('HTTP_COOKIE')
if not stored_cookie_string:
        print "Content-type: text/html"
        print
        notLoggedInPage()
else:
        cookie = Cookie.SimpleCookie(stored_cookie_string)
        if 'username' in cookie:
                aname = cookie['username'].value

                print "Content-type: text/html"
                print
                loggedInPage(aname)

        else:
                notLoggedInPage()

print '	</body>'
print '</html>'
