#import interface.frontEnd as FE
import mysql.connector

def connectMySQL():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ibd2024"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SHOW DATABASES")

  for database in mycursor:
        print(database)


def main():
  print("Baum!?")

if __name__ == "__main__":
  main()
  connectMySQL()
  #FE.showDatabases()