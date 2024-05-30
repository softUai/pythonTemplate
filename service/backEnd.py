import database.manipulate as DB

def databasesConnected():
    mydb = DB.connectMySQL()
    print(mydb)
    mycursor = mydb.cursor()
    

    # print("Into BackEnd")
    # for database in mycursor:
    #     print(database)
    
    return mycursor.execute("SHOW DATABASES")
    
