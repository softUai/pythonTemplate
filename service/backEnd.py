import database.connect as DB

def searchTables(dbName):
  db = DB.dbConnectByName(dbName)
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

def dropSchemEmpresa():
  conn = DB.dbConnect()
  cursor = conn.cursor()
  database_name = "empresa"
  drop_db_query = f"DROP DATABASE {database_name};"
  # Execute the SQL query
  cursor.execute(drop_db_query)
  print(f"Database '{database_name}' dropped successfully.")
    
