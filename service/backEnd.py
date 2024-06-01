import database.connect as DB

def searchTables(dbName):
  db = DB.dbConnect(dbName)
  mycursor = db.cursor()
  mycursor.execute("SHOW TABLES")
  return mycursor.fetchall()

def printTables(dbName):
   namesTablelist = searchTables(dbName)
   for name in namesTablelist:
      print(name[0])

def createSchemEmpresa():
  print("BE.createEmpresa")
  DB.createSchemV0()

def instancySchemEmpresa():
  print("BE.populateEmpresa")
  DB.populateSchemV0()
    
