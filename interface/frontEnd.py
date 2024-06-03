import service.backEnd as BE

def departmentData():
  nameDpt = input("Digite o nome do departamento: ") 
  numDpt = input("Digite o numero do departamento: ") 
  cpfManager = input("Digite o cpf do gerente do departamento: ") 
  startDateManager = input("Digite a data de inicio do gerente do departamento: ") 
  val = (nameDpt, numDpt, cpfManager, startDateManager)
  return val

def print_menu():
    print("1. Show tables from a database name")
    print("2. Create company's schem")
    print("3. Populate company's schem")
    print("4. Drop company's schem")
    print("5. Insert department")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            dbName = input("Enter database name: ")
            BE.printTables(dbName)
        elif choice == '2':
            BE.createSchemEmpresa()
        elif choice == '3':
            BE.instancySchemEmpresa()
        elif choice == '4':
            BE.dropSchemEmpresa()
        elif choice == '5':
            BE.insertDepartment()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()