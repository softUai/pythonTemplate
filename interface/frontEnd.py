import service.backEnd as BE

def departmentData():
  nameDpt = input("Digite o nome do departamento: ") 
  numDpt = input("Digite o numero do departamento: ") 
  cpfManager = input("Digite o cpf do gerente do departamento: '11 characteres' - ") 
  startDateManager = input("Digite a data de inicio do gerente do departamento: 'YYYY-MM-DD' - ") 
  val = (str(nameDpt), str(numDpt), str(cpfManager), str(startDateManager))
  return val

def print_menu():
    print("1. Create company's schem")
    print("2. Show relations")
    print("3. Insert department")
    print("4. Drop department by number")
    print("5. Add last constraint in department")
    print("6. Drop company's schem")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            BE.createSchemEmpresa()
        elif choice == '2':
            BE.printTables("empresa")
        elif choice == '3':
            BE.insertDepartment("empresa", departmentData())
        elif choice == '4':
            BE.insertDepartment("empresa", departmentData())
        elif choice == '5':
            BE.dropDepartmentByDnumero("empresa", departmentData())
        elif choice == '6':
            BE.dropSchemEmpresa()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()