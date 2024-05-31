import database.manipulate as DB

def tableList(dbName):
  db = DB.dbConnect(dbName)
  mycursor = db.cursor()
  mycursor.execute("SHOW TABLES")
  myresult = mycursor.fetchall()
  return myresult
    
