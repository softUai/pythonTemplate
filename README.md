# Pytho Template
This project is a Python language template with a five-layer architecture implementation and MySQL connection. The database used was a company, it was explained in Elmashi and Navathe book, introduction a database fundamentals, 7th edition.

# Start enviroment
- python -m venv pyenv
- .\pyenv\Scripts\activate
- Create layers (folders):
  - doc
  - database
  - interface
  - service
  - test
- Code construction 
  - database -> Implement a database connection and store sql's files.
  - service -> Implement a back end code.
  - interface -> Implement a front end code.
  - test -> Implement unit and functional tests code.
  - app.py -> Implement a executable code.

# If you install some library for example to MySQL connection
- python -m pip install mysql-connector-python
- pip freeze > doc\requirements.txt -> Generate the requirements.
- pip install -r doc\requirements.txt -> Execute the requirements from a file.

# Example
- A MVP was created from the company database and department relation. You can use a menu to use the program. To do that, execute python app.py.
- Choose a sequencial options:
  - 1. Create company's schem
  - 2. Show relations
  - 3. Insert department
        - Inputs: The program asks for one value each time.
          - ('Pesquisa', 5, '33344555587', '1988-05-22'),
          - ('Administração', 4, '98765432168', '1995-01-01'),
          - ('Matriz', 1, '88866555576', '1981-06-19');
          - ('None', 0, '12345678910', '1111-11-11');
  - 4. Drop department by number
        - Inputs: The program asks for one value each time.
          - 0
  - 5. Add last constraint in department
  - 6. Drop company's schem
  - 0. Exit

# Exercises
 - Complete the database with the others tubles by the instance showed in the book.
 - Implement some queries and modifications in database schem.