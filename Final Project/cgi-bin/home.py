#!"C:\Python27\python.exe"

# CSC210 - home - 11/18/2015
# Charlie Norvell

import cgitb
cgitb.enable()

##import cgi
##form = cgi.FieldStorage()
##title = form['title'].value
##url = form['id'].value

import sqlite3
import random
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
print "Content-type: text/html"
print

def notLoggedIn():
    #code from user Billy Moon on Stack Overflow
    #redirects to Login Page
    print '<html>'
    print '<head>'
    print ' <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
    print '    <meta charset="UTF-8">'
    print '    <meta http-equiv="refresh" content="1;url=login.py">'
    print '    <script type="text/javascript">'
    print '        window.location.href = "login.py"'
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
    print '        If you are not redirected automatically, follow the <a href="login.py">link to Sign In page</a>'
    print '</body>'
    print '</html>'

def loggedIn(aname):
    print '<!DOCTYPE html>'
    print '<html>'
    print '<head>'
    print ' <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
    print '    <title>Story</title>'
    print '    <script type = "text/javascript" src="https://apis.google.com/js/api.js"></script>'
    print '    <script src="https://www.gstatic.com/realtime/realtime-client-utils.js"></script>'
    print '''
    <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    '''
    print '    </head>'
    #django_browserid.helpers.browserid_logout(text='Log out', next=None, link_class='browserid-logout', attrs=None)
    print '''
  <body>
  <header>
      <ul style="position:fixed;">
          <li><a href="Story.py">Story</a></li>
          <li><a name="about" href="../Story.html#about">About</a></li>
          <li><a class="active" name="home" href="home.py">Story Home</a></li>
          <ul style="float:right;list-style-type:none;">
'''
    print       '<li><a href="profile.py?aname=' + aname +'">' + aname + '</a></li>'
    print '''
               <li><a href="../Update.html">Update Profile</a></li>
               <li><a href="delete.py">Delete Profile</a></li>
               <li><a href="logout.py">Log Out</a></li>
          </ul>
      </ul>
  </header>
  '''
    print '''
    <h2>Story Home</h2>
    <p style="text-align:center;">
     <button id="auth_button" class="button" style="width:450px;height:30px;">
        Authorize your Google account to start your Writing Journey</button>
    </p>
    <br>
    <br>
     <a href="../New.html" class="button" style="width:450px;height:30px;font-size:15px;">
         Start your new story</a>
    <br>
    <br>
    <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Title</th>
        <th>Description</th>
        <th>Link to the Story</th>
      </tr>
    </thead>
    <tbody>
    '''
    x = 1;
    for r in c.execute('select * from documents;'):
        print ' <tr>'
        print '     <td>'+str(x)+'</td>'
        print '     <td>'+r[0]+'</td>'
        print '     <td>'+r[3]+'</td>'
        print '    <td><a href="writing.py?id='+r[1]+'" class="button">Write this</a></td>'
        print ' </tr>'
        x+=1
    print '''
    </tbody>
  </table>
  </body>
</html>
'''

import Cookie
import os
import time

stored_cookie_string = os.environ.get('HTTP_COOKIE')
if not stored_cookie_string:
    notLoggedIn()

else:
    cookie = Cookie.SimpleCookie(stored_cookie_string)
    if 'username' in cookie:
        aname = cookie['username'].value
        loggedIn(aname)
##        if 'id' in form:
##            c.execute('insert into documents values (?, ?, ?)', (title, url, aname))
##            conn.commit()
##            print 'saved!'

    else:
        print "Content-type: text/html"
        print # don't forget the extra newline!
        notLoggedIn()

conn.close()
