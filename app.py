import interface.frontEnd as FE
import pyenv.private as pvt
import mysql.connector

def main():
  mydb = mysql.connector.connect( host=pvt.HOST, user=pvt.USER, password=pvt.PASSWORD, database="empresa")
  mycursor = mydb.cursor()

  with open('database/populaDB.sql', 'r') as file:
      createSQLScript = file.read()
  
  sqlScript = createSQLScript.split(";")
  print(sqlScript[0] + ";")

  sql = "INSERT INTO departamento VALUES (%s, %s, %s, %s)"
  val = ('Pesquisa', 5, '33344555587', '1988-05-22')
  mycursor.execute(sql, val)

  mydb.commit()

  mydb.close()
  mycursor.close()

if __name__ == "__main__":
  main()

