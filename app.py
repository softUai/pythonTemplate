import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ibd2024"
)

print(mydb)