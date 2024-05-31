import service.backEnd as BE

def printTables(dbName):
   namesTablelist = BE.tableList(dbName)
   for name in namesTablelist:
      print(name[0])