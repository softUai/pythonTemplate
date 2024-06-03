import database.connect as DB
from mysql.connector import Error as dbError

def searchTables(dbName):
  result = []
  try:
    db = DB.dbConnectByName(dbName)
    mycursor = db.cursor()
    mycursor.execute("SHOW TABLES")
    result = mycursor.fetchall()
    return result
  except dbError as e:
    print(f"Error while connecting to MySQL by database name: {e}")
  finally:
    return result
  
def printTables(dbName):
   namesTablelist = searchTables(dbName)
   for name in namesTablelist:
      print(name[0])

def createSchemEmpresa():
  print("BE.createEmpresa")
  DB.createSchemV0()

def dropSchemEmpresa():
  conn = DB.dbConnect()
  cursor = conn.cursor()
  database_name = "empresa"
  drop_db_query = f"DROP DATABASE {database_name};"
  # Execute the SQL query
  cursor.execute(drop_db_query)
  print(f"Database '{database_name}' dropped successfully.")

def insertDepartment(dbName, val):
  db = DB.dbConnectByName(dbName)
  mycursor = db.cursor()
  sql = "INSERT INTO departamento VALUES (%s, %s, %s, %s)"
  mycursor.execute(sql, val)
  mycursor.fetchall()
  db.commit()

def dropDepartmentByDnumero(numDept):
  db = DB.dbConnectByName("empresa")
  mycursor = db.cursor()
  sql = "DELETE FROM departamento Where Dnumero = (%s)"
  val = [(numDept)]
  mycursor.execute(sql, val)
  mycursor.fetchall()
  db.commit()

def addConstraintCpfGerente():
  db = DB.dbConnectByName("empresa")
  mycursor = db.cursor()
  #sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
  sql = "ALTER TABLE departamento ADD CONSTRAINT FK_cpf_gerente FOREIGN KEY (cpf_gerente) REFERENCES Funcionario (cpf) ON DELETE CASCADE ON UPDATE CASCADE;"
  mycursor.execute(sql)
  mycursor.fetchall()
  db.commit()
