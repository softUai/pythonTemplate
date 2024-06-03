import interface.frontEnd as FE
import pyenv.private as pvt
import mysql.connector
from mysql.connector import Error as dbError

def main():
  mydb = mysql.connector.connect( host=pvt.HOST, user=pvt.USER, password=pvt.PASSWORD, database="empresa")
  mycursor = mydb.cursor()

  sql = "INSERT INTO departamento VALUES (%s, %s, %s, %s)"
  val = ('None', '0', '11100022233', '1111-11-11')

  mycursor.execute(sql, val)

  mydb.commit()

  mydb.close()
  mycursor.close()


if __name__ == "__main__":
  try:
    main()
  except dbError as e:
        print(f"Error while connecting to MySQL: {e}")
  finally:
    print("Finish the program!")

