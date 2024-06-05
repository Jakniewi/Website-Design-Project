import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password"
)
 
# Printing the connection object 
print(mydb)