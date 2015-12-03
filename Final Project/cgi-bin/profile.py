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
print '<h2>'+aname+'\'s Profile</h2>'
#find and print out user's information
for r in c.execute('select * from accounts;'):
    if (r[0] == aname):
        print '<h3>Name: '+r[1]+' '+r[2]+'</h3>'
        print '<h3>Talent: '+r[5]+'</h3>'
        print '<img src="'+r[4]+'"/>'
print '<p><button id="auth_button">Authorize your Google account</button></p>'
print '<p><a href="home.py">New Story</a></p>'
print '<p><a href="../Update.html">Update Profile</a></p>'
print '<p><a href="logout.py">Log Out</a></p>'
print '<p><a href="delete.py">Delete Account</a></p>'

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

print '''
    <script>
        var clientID='754145444518-q7ucn0o0jr3m2ae69ogqt1orqgublnn1.apps.googleusercontent.com';
        if (!/^([0-9])$/.test(clientId[0])) {
            alert('Invalid Client ID - did you forget to insert your application Client ID?');
        }
        // Create a new instance of the realtime utility with your client ID.
        var realtimeUtils = new utils.RealtimeUtils({ clientId: clientId });

        authorize();

        function authorize() {
            // Attempt to authorize
             realtimeUtils.authorize(function(response){
              if(response.error){
                // Authorization failed because this is the first time the user has used your application,
                // show the authorize button to prompt them to authorize manually.
                var button = document.getElementById('auth_button');
                button.classList.add('visible');
                button.addEventListener('click', function () {
                  realtimeUtils.authorize(function(response){
                  }, true);
                });
              } else {
                  start();
              }
            }, false);
        }
'''

print '	</body>'
print '</html>'
