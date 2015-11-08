#!"C:\Python27\python.exe"

# CSC210 - Profile Page - 11/08/2015
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

aname = form['aname'].value

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
print '			'+aname+'\'s Profile'
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
print '<h1>'+aname+'\'s Profile</h1>'
#find and print out user's information
for r in c.execute('select * from accounts;'):
    if (r[0] == aname):
        print '<h2>Name: '+r[1]+' '+r[2]+'</h2>'
        print '<h2>Talent: '+r[5]+'</h2>'
        print '<img src="'+r[4]+'"/>'
print '<hr><h3>Other Users:</h3>'

# print out the data for all users in the database
for r in c.execute('select * from accounts;'):
    if (r[0] != aname):
        firstname = r[1];
        lastname = r[2];
        wrt = r[5];
        img = r[4];
        print '<h3>Name: '+firstname+' '+lastname
        print '<br>Talent: '+wrt
        print '<br><img src="'+img+'"/>'
        print '</h3>'
        
conn.close()

print '	</body>'
print '</html>'
