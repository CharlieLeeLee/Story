#!"C:\Python27\python.exe"

# CSC210 - log in - 11/08/2015
# Charlie Norvell

# To run, start AMPSS and visit URLs like the following to insert new
# entries into the database, then check your database's contents using
# lecture4-query-database.py
#
# http://localhost/cgi-bin/lecture4.py?my_name=Joe&my_age=32&my_image=../cat.jpg
# http://localhost/cgi-bin/lecture4.py?my_name=Donna&my_age=37&my_image=../dog.jpg

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

aname = form['accountname'].value
pw = form['password'].value


# insert new user data into the database
import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

print '<html>'
print ' <head>'
print '		<title>'
print '			Sign In Error'
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
print '<h1>Logging In...</h1>'

# print out the data for all users in the database
notfound = True
for r in c.execute('select * from accounts;'):
        if (r[0] == aname):
            notfound = False
            if(r[3] == pw):
                print '<meta http-equiv="refresh"'
                print ' content="0; url=profile.py?aname='+aname+'">'
            else:
                print '<h2> Incorrect Password</h2>'
                print '<a href="../SignIn.html">Try Again</a>'
if (notfound):
    print '<h2>User '+aname+' does not exist.</h2>'
    print '<h2><a href="../CreatAccount.html">Create New Account</a></h2>'
else:
    print '<h2>Redirecting...</h2>'
conn.close()

print '	</body>'
print '</html>'
