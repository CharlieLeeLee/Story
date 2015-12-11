#!"C:\Python27\python.exe"

# CSC210 - home - 11/18/2015
# Yumeng Liu

import time
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()
import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
if ('id' in form):
    for r in c.execute('SELECT * from documents WHERE address=?', (form['id'].value,)):
        title = r[0]
        desc = r[3]
    new = False
else:
    title = form['title'].value
    desc = form['description'].value
    new = True

import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# ...


# Path to client_secret.json which should contain a JSON document such as:
#   {
#     "web": {
#       "client_id": "[[YOUR_CLIENT_ID]]",
#       "client_secret": "[[YOUR_CLIENT_SECRET]]",
#       "redirect_uris": [],
#       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#       "token_uri": "https://accounts.google.com/o/oauth2/token"
#     }
#   }
CLIENTSECRET_LOCATION = 'client_secret_754145444518-q7ucn0o0jr3m2ae69ogqt1orqgublnn1.apps.googleusercontent.com.json'
REDIRECT_URI = 'http://localhost:80/oauth2callback'
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.appdata'
]
APPLICATION_NAME = 'Story'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENTSECRET_LOCATION, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v2', http=http)

request = service.files().generateIds(maxResults = 1, space = 'drive').execute()
url = request.get('ids', [])[0]


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
  <script type="text/javascript" src="https://apis.google.com/js/client.js?onload=handleClientLoad"></script>
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
    print '    <main>'
    print '    <h2>'+title+'</h2>'
    print '''
    <h3>
      <br><textarea id="text_area_1"></textarea>
      <br>
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
                   makeApiCall() }, true);
                });

              } else {
                  makeApiCall();
              }
            }, false);
      }
      function makeApiCall() {
          gapi.client.load('drive', 'v2', start);
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
            gapi.client.drive.files.insert({
                'resource':
                {
                    'mimeType': 'application/vnd.google-apps.drive-sdk',
    '''
    print "                'id':'"+url+"',"
    print "                'title':'"+title+"',"
    print "                'description':'"+desc+"'"
    print '''
                }
            }).execute(function (insertresponse)
            {'''
    print "             window.history.pushState(null, null, '?id="+url+"');"
    print "                realtimeUtils.load('"+url+"', onFileLoaded, onFileInitialize);"
    print '            });'
    print '        }'
    print '      }'
    print '''

      // The first time a file is opened, it must be initialized with the
      // document structure. This function will add a collaborative string
      // to our model at the root.
      function onFileInitialize(model) {
        var string = model.createString();
        string.setText('Start Your Story Here');
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
        if (new):
            c.execute('INSERT INTO documents VALUES(?,?,?,?)', (title, url, aname, desc))
            conn.commit()
        loggedIn(aname)
        
    else:
        notLoggedIn()

conn.close()
