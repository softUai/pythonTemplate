import service.backEnd as BE

def departmentData():
  nameDpt = input("Enter the name of the department: '45 characters' -> ") 
  numDpt = input("Enter the number of the department: 'interger' -> ")
  cpfManager = input("Enter the cpf of the department's manager:: '11 caracteres' -> ") 
  startDateManager = input("Enter the start dat of the department's manager: 'YYYY-MM-DD' -> ") 
  val = (str(nameDpt), str(numDpt), str(cpfManager), str(startDateManager))
  return val

def print_menu():
	print("\n---------------------Welcome--------------------------------")
	print("1. Create company's schem")
	print("2. Show relations")
	print("3. Insert department")
	print("4. Drop department by number")
	print("5. Add last constraint in department")
	print("6. Drop company's schem")
	print("0. Exit")
	print("---------------------Database Company------------------------\n")

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
			numDpt = input("Digite o numero do departamento: ")
			BE.dropDepartmentByDnumero(numDpt)
		elif choice == '5':
			BE.addConstraintCpfGerente()
		elif choice == '6':
			BE.dropSchemEmpresa()
		elif choice == '0':
			print("Exiting...")
			break
		else:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()