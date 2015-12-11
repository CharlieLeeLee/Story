#!"C:\Python27\python.exe"

# CSC210 - Profile Page - 11/08/2015
# Charlie Norvell

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

aname = form['aname'].value

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
print '		<link rel="stylesheet" type="text/css" href="../Styles/style.css">'
print '    <script src="https://apis.google.com/js/api.js"></script>'
print '    <script src="https://www.gstatic.com/realtime/realtime-client-utils.js"></script>'
print ' </head>'

print '<body>'
print '''
<header>
    <ul style="position:fixed;">
        <li><a href="Story.py">Story</a></li>
        <li><a name="about" href="../Story.html#about">About</a></li>
        <li><a name="home" href="home.py">Story Home</a></li>
        <ul style="float:right;list-style-type:none;">
'''
print       '<li><a class="active" href="profile.py?aname=' + aname +'">' + aname + '</a></li>'
print '''
             <li><a href="../Update.html">Update Profile</a></li>
             <li><a href="delete.py">Delete Profile</a></li>
             <li><a href="logout.py">Log Out</a></li>
        </ul>
    </ul>
</header>
'''
print '<h2>Hello, '+aname+'</h2>'
#find and print out user's information
for r in c.execute('select * from accounts;'):
    if (r[0] == aname):
        print '<div style="float:left;height:400px;width:45%;">'
        print '  <div id="profilepic">'
        print '  <img src="'+r[4]+'"/>'
        print '  </div>'
        print '</div>'
        print '<div style="float:right;height:400px;width:55%;">'
        print '<div id="profileinfo">'
        print '  <h4>Name: '+r[1]+' '+r[2]+'</h4>'
        print '  <h4>Talent: '+r[5]+'</h4>'
        print '  </div>'
        print '</div>'

print '<hr><h3 style="text-align:left;">Other Users:</h3>'
print '<br><br>'
# print out the data for all users in the database
for r in c.execute('select * from accounts;'):
    if (r[0] != aname):
        print '<div style="float:left;height:400px;width:25%;">'
        print '  <div id="profilepic">'
        print '  <img src="'+r[4]+'"/>'
        print '  </div>'
        print '</div>'
        print '<div style="float:right;height:400px;width:75%;">'
        print '<div id="profileinfo">'
        print '  <h3>Name: '+r[1]+' '+r[2]+'</h3>'
        print '  <h3>Talent: '+r[5]+'</h3>'
        print '  </div>'
        print '</div>'

conn.close()
print '	</body>'
print '</html>'
