import mysql.connector
import pyenv.private as pvt

def dbConnect(dbName):
  return mysql.connector.connect( host=pvt.HOST, user=pvt.USER, password=pvt.PASSWORD, database=dbName )

