import service.backEnd as BE

def showDatabases():
    connections = BE.showDatabasesConnected()
    for database in connections:
        print(database)