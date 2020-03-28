# Week 4: ORMs, APIs

## Object-Oriented Programming

* 3:30: classes0.py - defined a Python flight class
* 5:35: classes1.py - created a new flight and print out details
* 12:30: classes2.py - added print_info method to flight class
* 17:10: classes3.py - added a method for adding a delay to the flight
* 19:45: classes4.py - added passengers class & linked it to the flight class

## Object-Relational Mapping (ORM)

* Allows you to use Python structures and interact with SQL databases
* 27:40: models.py - example written with flask-sqlalchemy
  * class `Flight()` inherits from `db.Model` in SQLAlchemy - this allows for
  built-in relationships between Flask & SQLAlchemy
  * `db.create_all()` takes all your classes and converts them into SQL tables
  in SQLAlchemy
* 32:45: create.py - creates a database via Flask
* 39:15: import1.py - a file to add data to database using a python for loop &
SQLAlchemy ORM
* 40:25: list1.py - select query using SQLAlchemy ORM
* Usefulness of ORMs is that it allows you make your Python code more complex,
but don't need to worry about writing complicated SQL queries
* 52:20: airline1 - Flask app to create a website to allow people to register
for flights using SQLAlchemy ORMs
* 57:20: airline3 - updating the Flask app above with the ability to add
passengers to flights
* 1:00:30: airline4 - updating the Flask app above with a relationship to the
passengers table
* 1:03:40: the syntax that shows how to select passengers using the Flight
class

## Application Programming Interfaces (APIs)

### JSON

* A way of representing information in a human-readable format as well as a
computer-readable format that is easy to pass between programs
* 1:11:55: Nested JSON objects
* 1:16:55: google.py - file that prints a get request to google.com
* 1:19:30: fixer.io - a foreign exchange rate API
* 1:21:40: currency0.py - queries the fixer.io API and prints out exchange rates
in JSON format
* Common status codes:
  * 200: OK
  * 201: Created
  * 400: Bad Request
  * 403: Forbidden
  * 404: Not Found
  * 405: Method Not Allowed
  * 422: Unprocessable Entity
* 1:25:45: currency1.py - updates above file & prints out response in a more
human readable format
* 1:30:25: currency2.py - updates above file & allows you to select your base &
exchange currency
* 1:33:50: airline5 - building an API route in the flights Flask app to allow a
get request to return info on a given flight
