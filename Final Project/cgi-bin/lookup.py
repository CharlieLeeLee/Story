#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# CSC 210 - Lookup - 12/11/2015
# Charlie Norvell

# To run, start AMPSS and visit URLs like the following:

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

query = form['search_input'].value

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
x = 0
data = []
results = {}
            
            

for r in c.execute("select * from accounts where aname = ? or fname = ? or lname = ?;", (query, query, query)):
	aname = r[0]
	fname = r[1]
	lname = r[2]
	pic = r[4]
	talent = r[5]
	#print name + ' ' + str(age) + ' ' + image

        results['accountname'] = aname
        results['firstname'] = fname
        results['lastname'] = lname
        results['writingtalent'] = talent
        results['profile'] = pic
        data.append(results)
        print results
	
#	results['accountname'].append(str(x)+': '+aname)
#	results['firstname'].append(str(x)+': '+fname)
#	results['lastname'].append(str(x)+': '+lname)
#	results['writingtalent'].append(str(x)+': '+talent)
#	results['profile'].append(str(x)+': '+pic)

#print json.dumps(data)

conn.close()
