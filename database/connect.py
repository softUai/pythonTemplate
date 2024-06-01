import mysql.connector
import pyenv.private as pvt

def dbConnect(dbName):
  return mysql.connector.connect( host=pvt.HOST, user=pvt.USER, password=pvt.PASSWORD, database=dbName )

def createEmpresaDB():
  with open('database/createDB.sql', 'r') as file:
      createSQLScript = file.read()
  print(createSQLScript)
  return createSQLScript

def populateEmpresaDB():
  with open('database/populaDB.sql', 'r') as file:
      populaSQLScript = file.read()
  print(populaSQLScript)
  return populaSQLScript