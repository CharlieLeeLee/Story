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
    print '        If you are not redirected automatically, follow the <a href="login.py">link to Sign In page</a>'
    print '</body>'
    print '</html>'

def loggedIn():
    print '<html>'
    print '<head>'
    print ' <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>'
    print '    <title>Story</title>'
    print '    <script type = "text/javascript" src="https://apis.google.com/js/api.js"></script>'
    print '    <script src="https://www.gstatic.com/realtime/realtime-client-utils.js"></script>'
    print '    </head>'
    #django_browserid.helpers.browserid_logout(text='Log out', next=None, link_class='browserid-logout', attrs=None)
    print '''
  <body>
    <main>
      <h2>Story</h2>
      <br><textarea id="text_area_1"></textarea>
      <br>
      <button id="saveButton">Save</button>
    </main>
    
    <script>
      var clientId = '754145444518-q7ucn0o0jr3m2ae69ogqt1orqgublnn1.apps.googleusercontent.com';

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
                // show the authorize button to prompt them to authorize manually.
                var button = document.getElementById('auth_button');
                button.classList.add('visible');
                button.addEventListener('click', function () {
                  realtimeUtils.authorize(function(response){
                   start() }, true);
                });
                
              } else {
                  start();
              }
            }, false);
        }

      function start() {
        // With auth taken care of, load a file, or create one if there
        // is not an id in the URL.
        var id = realtimeUtils.getParam('id');
        if (id) {
          // Load the document id from the URL
          realtimeUtils.load(id.replace('/', ''), onFileLoaded, onFileInitialize);
        } else {
          // Create a new document, add it to the URL
          realtimeUtils.createRealtimeFile('New Quickstart File', function(createResponse){
              window.history.pushState(null, null, '?id=' + createResponse.id);
              realtimeUtils.load(createResponse.id, onFileLoaded, onFileInitialize);
          });
                   }
      }

      // The first time a file is opened, it must be initialized with the
      // document structure. This function will add a collaborative string
      // to our model at the root.
      function onFileInitialize(model) {
        var string = model.createString();
        string.setText('Welcome to the Story!');
        model.getRoot().set('demo_string', string);
      }

      // After a file has been initialized and loaded, we can access the
      // document. We will wire up the data model to the UI.
      function onFileLoaded(doc) {
        var collaborativeString = doc.getModel().getRoot().get('demo_string');
        wireTextBoxes(collaborativeString);
      }

      // Connects the text boxes to the collaborative string
      function wireTextBoxes(collaborativeString) {
        var textArea1 = document.getElementById('text_area_1');
        gapi.drive.realtime.databinding.bindString(collaborativeString, textArea1);
      }
    </script>
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
        loggedIn()
##        if 'id' in form:
##            c.execute('insert into documents values (?, ?, ?)', (title, url, aname))
##            conn.commit()
##            print 'saved!'
            
    else:
        print "Content-type: text/html"
        print # don't forget the extra newline!
        notLoggedIn()
        
conn.close()
