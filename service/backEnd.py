import database.manipulate as DB

def showDatabasesConnected():
    mycursor = DB.connectMySQL()
    mycursor.execute("SHOW DATABASES")
    return mycursor