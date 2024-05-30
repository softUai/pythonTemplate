def connectMySQL():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ibd2024"
  )

#   mycursor = mydb.cursor()
#   mycursor.execute("SHOW DATABASES")

#   for database in mycursor:
#         print(database)

  return mydb