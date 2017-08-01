'''
This program takes an input file that contains instructions on how do
divide the fields by experiment. The program then outputs the experiments
in separate CSV files.

The delimiters file that is used for this program must share the exact some
format as all other ones before it, else this program will not run.

Created by Luke Steffen
Created on 07/25/2017
'''

import sqlite3 as sql
import csv as csv

'''This beginning portion of the code establishes connections to the databases and establishes the 
delimiters file from which the data will be written to.'''
database = input("Please enter the filepath of the database: ")

db = sql.connect(database)
cur = db.cursor()

db2 = sql.connect("Experiments.db")
cur2 = db2.cursor()

file = input("Please enter the filepath of the field delimiters file: ")

'''These with and for loop statements collect to data from the delimiters file and sets it up 
into a list for further use.''' 
guide = []
with open(file) as f:
    for line in f:
        guide.append(line.strip().split('\t'))

#Removes the column names from the list so it doesn't interfere with the process
guide.remove(['Name', 'PlotStart', 'PlotEnd', 'TraitsContain'])
 
#Converts strings to intergers to help manipulate data
for g in guide:
    g[1] = int(g[1])
    g[2] = int(g[2])
 

#Get all the data from the database and place it into a list
cur.execute("SELECT rid, parent, userValue, timeTaken FROM user_traits")
output = cur.fetchall()


'''Main loop that splits the data by experiment title and delimiters. First, a loop is created that checks to see
if the range of the rid is within range of the specific start and end plots. Then, the delimiters are pulled,
saving the letter in the front, converting the numbers to intergers from strings. It then increments
through the two numbers filling in the missing numbers (Ex: a delimeter of 1:4 would become a list of 1, 2, 3, 4).
The loop then converts the numbers back to strings and places the letter back into the string. Finally, a nested
for loop checks the parent column of each row in the data to see if the specified strings are contained within the
name of the file (Ex: the program is looking for D1, D2, D3, D4 within each parent name). It then places these data
points into a new list. This new list is written to the CSV file. If there are no delimiter ranges (traitscontain is
NA), a check for the rid range is run and the rows of data are written to a CSV file.'''
for g in guide:
#     print(g[1], g[2])
#Creates a table, currently there is no use for the table, however it can be implemented
    query = "CREATE TABLE " + g[0] + " (rid, parent, userValue, timeTaken)"
    cur2.execute(query)
    plots = []
    for row in output:
        if(g[1] < int(row[0]) < g[2]):
            plots.append(row)
    #Check to see of traitscontain is NA, if so converting and writing is not necessary
    if (g[3] == 'NA'):
        with open(str(g[0]) + ".csv", 'w', newline='') as csvFile:
            w = csv.writer(csvFile, dialect='excel')
            w.writerow(["rid", "parent", "userValue", "timeTaken"])
            w.writerows(plots)
            print(str(g[0]) + " has been written.")
    else:
        #establishment of empty lists for later use
        ints = []
        strngs = []
        num = []
        final = []
        data = []
        #split the traitscontian entry by the colon (D1:D4 -> [D1, D4])
        param = g[3].split(':')
        #pull the letter out of the list, making it just a number
        for point in param:
            for char in point:
                if (char == "D" or char == "W"):
                    letter = char
                else:
                    num.append(char)
        #Checks to see if there are multiple digit numbers and combines the second and third list entry
        if (len(num) >= 3):
            num[1] = num[1] + num[2]
            num.remove(num[2])
        #Converts the string numbers to interger numbers
        for point in num:
            ints.append(int(point))
        num = ints
        #Loops through and fills in the numbers between the first and last number
        i = num[0]
        while (i < num[1]):
            if (i != num[0] and i != num[1]):
                num.append(i)
            i += 1
        #Convert the interger back to a string and add the letter back onto the string
        for n in num:
            final.append(letter + str(n))
        num = final
        #Check to see if the traitscontain parameter is within the parent name
        for row in output:
            for nu in num:
                if (nu in row[1]):
                    data.append(row)
        #Write the data to a CSV file with the name of the experiment name.
        with open(str(g[0]) + ".csv", 'w', newline='') as csvFile:
            w = csv.writer(csvFile, dialect='excel')
            w.writerow(["rid", "parent", "userValue", "timeTaken"])
            w.writerows(data)
        print(str(g[0]) + " has been written.")
                




