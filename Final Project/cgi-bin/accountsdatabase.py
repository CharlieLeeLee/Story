#!"C:\Python27\python.exe"

# CSC210 -creat database - 11/08/2015
# Yumeng Liu

# To create a database named accounts.db, run:
#
# python create-database.py


import sqlite3

# create a database file named 'accounts.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# create a new 'accounts' table with six columns: fname, lname,aname,pw,image,writing
c.execute('create table accounts(aname varchar(100) primary key, fname varchar(100), lname varchar(100), pw varchar(100), image varchar(100), writing varchar(10))')

# insert 3 rows of data into the 'users' table
#c.execute("insert into users values('Philip', 30, '../cat.jpg');")

# commit ('save') the transaction and close the connection
conn.commit()
conn.close()
