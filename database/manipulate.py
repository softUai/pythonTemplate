import mysql.connector

def dbConnect(dbName):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ibd2024",
    database=dbName
  )
  return mydb