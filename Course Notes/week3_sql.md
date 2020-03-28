# Week 3: SQL

* 4:30: CREATE TABLE
* 11:10: INSERT INTO
* 21:30: SQL Functions
* 33:10: adminer.cs50.net
* 44:20: Joins
* 50:15: Indexing
* 54:55: Nested queries
* 57:10: SQL Injection
  * When running SQL queries with user input, you don't want to directly
  substitute the user's input into your query, this can lead to SQL injection
  attacks, you want to 'sanitize' the input before you run the query
1:03:00: Race Conditions
  * Concurrent queries can lead to issues with changing/updating databases
  * SQL transactions begin a query, lock the DB, then commit the query so you
  are not able to simultaneously query the same table at the same time
* 1:09:15: SQLAlchemy
  * When running an insert query, db.execute() will keep track of all the
  changes you want to make, but it won't submit them to the database until you
  call db.commit
1:25:15: airline0 - a Flask app that shows flights & allows you to book a flight
1:38:35 : airline1 - extending airline0 to see the current passengers on a
flight
