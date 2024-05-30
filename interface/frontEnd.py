import service.backEnd as BE

def showDatabases():
    mycursor = BE.databasesConnected()
    print(mycursor)
    print("Into FrontEnd")
    for database in mycursor:
        print(database)