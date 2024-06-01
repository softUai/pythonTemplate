import service.backEnd as BE

def printTables(dbName):
   namesTablelist = BE.searchTables(dbName)
   for name in namesTablelist:
      print(name[0])

def createEmpresa():
   print("FE.createEmpresa")
   BE.createEmpresa()