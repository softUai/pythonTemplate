# Pytho Template
This project is a Python language template with a five-layer architecture implementation and MySQL connection. The database used was the company, it was explained in Elmashi and Navathe book, introduction a database fundamentals, 7th edition.

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