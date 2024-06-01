import interface.frontEnd as FE
import pyenv.private as pvt
import mysql.connector

def createSchemV0(dbName):
  try:
    conn = mysql.connector.connect( host=pvt.HOST, user=pvt.USER, password=pvt.PASSWORD ) #Connect to MySQL database
    cursor = conn.cursor()

    with open('database/createDB.sql', 'r') as file:
      createSQLScript = file.read()
    
    # Execute the SQL script
    for statement in createSQLScript.split(';'):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
  
  except mysql.connector.Error as e:
    # Handle any MySQL errors
    print(f"MySQL error: {e}")

  except Exception as e:
    # Handle any exceptions
    print(f"An error occurred: {e}")

  finally:
    # Close the connection
    if conn:
        cursor.close()
        conn.close()
    

def main():
  print("baum")

if __name__ == "__main__":
  createSchemV0()
