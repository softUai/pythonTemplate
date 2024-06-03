import service.backEnd as BE

def print_menu():
    print("1. Show tables from a database name")
    print("2. Create Schem of the Company")
    print("3. Populate Schem of the Company")
    print("4. Drop Schem of the Company")
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
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()