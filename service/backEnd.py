import database.connect as DB

def searchTables(dbName):
  db = DB.dbConnect(dbName)
  mycursor = db.cursor()
  mycursor.execute("SHOW TABLES")
  return mycursor.fetchall()

def createEmpresa():
  print("BE.createEmpresa")
  DB.createEmpresaDB()
    
