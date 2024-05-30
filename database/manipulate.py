def connectMySQL():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ibd2024"
  )

  mycursor = mydb.cursor()  
  return mycursor