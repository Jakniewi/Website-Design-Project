import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="HasloMaslo123",
)

myCursor = mydb.cursor()

fd = open('baza.sql','r')
sqlFile = fd.read()
fd.close()

myCursor.execute(sqlFile)