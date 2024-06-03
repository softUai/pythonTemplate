# Pytho Template
This project is a Python language template with a five-layer architecture implementation and MySQL connection. The database used was the company, it was explained in Elmashi and Navathe book, introduction a database fundamentals, 7th edition.

# Start enviroment
- python -m venv pyenv
- .\pyenv\Scripts\activate
- create layers (folders):
  - doc
  - database
  - interface
  - service
  - test
- create app.py file
  - print("Baum?!") -> Implement a simple code.

# If you install some library for example to MySQL connection
- python -m pip install mysql-connector-python
- pip freeze > doc\requirements.txt -> Generate the requirements.
- pip install -r doc\requirements.txt -> Execute the requirements from a file.