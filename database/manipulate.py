import mysql.connector

def dbConnect(dbName):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ibd2024",
    database=dbName
  )
  return mydb

def showTables(dbName):
  db = dbConnect(dbName)
  mycursor = db.cursor()
  mycursor.execute("SHOW TABLES")
  return mycursor.fetchall()