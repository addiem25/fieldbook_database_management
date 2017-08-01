'''
This file is explicit code for merging databases by table.
This code merges by writing to a new database.

Created by Luke Steffen
Created on 06/15/2017
'''


'''
The following comment is an instruction on how to use this program.

WARNING: This code will only work if all of the column and table names are the same
throughout each database. Any change of column name or table name (including capitol letters) will
break this program. In order for the best possible outcome, keep table and column
names the same.

To change the database you wish to write to, change the filepath of the variable con.
To change the database you wish to write from, change the filepath of the variable con2.

If you are adding to a database that has already been created, comment out the lines that
have a note on them saying that this should be commented out (look for a line with # at the start).
If you are creating a new database, DO NOT comment out the lines, leave them there.

NOTE: the lines of note are lines 50, 62, 74, and 86. (if the comments are not one line
above each of the stated lines, ignore this.)

NOTE: to comment out, place a # at the beginning of the line.

If everything has gone well, you should see four lines saying 'Data has been written' in
the console.

Luke Steffen 

'''

import sqlite3 as sql

con = sql.connect("databases2017-3/test.db")
con2 = sql.connect("databases2017-3/Green2.db")

c = con.cursor()
c2 = con2.cursor()


c2.execute("SELECT rid, parent, trait, userValue, timeTaken FROM user_traits")
output = c2.fetchall()

#Comment out the line below if you are using a database that already exists
# c.execute("CREATE TABLE user_traits(rid, parent, traits, userValue, timeTaken)")
c.execute("BEGIN")
for row in output:
    c.execute("INSERT INTO user_traits VALUES (?, ?, ?, ?, ?)", row)
con.commit()
print("Data has been written")

c.execute("SELECT * FROM user_traits ORDER BY rid")
con.commit()

print("Database has been sorted by rid.")



'''
c2.execute("SELECT * FROM android_metadata")
output = c2.fetchall()

#Comment out the line below if you are using a database that already exists
c.execute("CREATE TABLE android_metadata(locale)")
c.execute("BEGIN")
for row in output:
    c.execute("INSERT INTO android_metadata VALUES (?)", row)
con.commit()
print("Data has been written")


c2.execute("SELECT trait, format, defaultValue, minimum, maximum, details, categories, isVisible, realPosition FROM traits")
output = c2.fetchall()

#Comment out the line below if you are using a database that already exists
c.execute("CREATE TABLE traits(trait, format, defaultValue, minimum, maximum, details, categories, isVisible, realPosition)")
c.execute("BEGIN")
for row in output:
    c.execute("INSERT INTO traits VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
con.commit()
print("Data has been written")


c2.execute("SELECT Plot, Row, Ran, Rep, Block, Entry, Name FROM range")
output = c2.fetchall()

#Comment out the line below if you are using a database that already exists
c.execute("CREATE TABLE range(Plot, Row, Ran, Rep, Block, Entry, Name)")
c.execute("BEGIN")
for row in output:
    c.execute("INSERT INTO range VALUES (?, ?, ?, ?, ?, ?, ?)", row)
con.commit()
print("Data has been written")'''




