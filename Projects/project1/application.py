import os
import requests
from dotenv import load_dotenv
from collections import namedtuple
import json

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")

    if request.method == "POST":
        # Query Books Postgres DB to get book data
        search_string = request.form.get("search-term")
        search_data = db.execute("""SELECT * from "Books" Where isbn LIKE :search_string
                                        UNION
                                    SELECT * from "Books" WHERE UPPER(title) LIKE UPPER(:search_string)
                                        UNION
                                    SELECT * from "Books" WHERE UPPER(author) LIKE UPPER(:search_string)
                                    """, {"search_string": f"%{search_string}%"}).fetchall()

        # Parse data from query
        titles = [row[1] for row in search_data]
        authors = [row[2] for row in search_data]
        years = [row[3] for row in search_data]
        isbns = [row[0] for row in search_data]

        # Get reviews from Goodreads
        load_dotenv(override=True)
        KEY = os.getenv('key')
        url = 'https://www.goodreads.com/book/review_counts.json'
        params = {"key": KEY, "isbns": ','.join(isbns)}
        response = requests.get(url, params=params)
        goodreads_data = response.json()

        # Parse data from Goodreads into lists to pass to results template
        avg_ratings_dict = {}
        ratings_count_dict = {}
        for book in goodreads_data.get('books'):
            isbn_ref = book.get('isbn')
            avg_rating = book.get('average_rating')
            ratings_count = book.get('work_ratings_count')
            avg_ratings_dict[isbn_ref] = avg_rating
            ratings_count_dict[isbn_ref] = ratings_count

        # Create lists to store data to pass to results template
        avg_ratings = []
        ratings_counts = []
        for rating_isbn, isbn in zip(avg_ratings_dict.keys(), isbns):
            if rating_isbn == isbn:
                avg_ratings.append(avg_ratings_dict[isbn])
        for rating_isbn, isbn in zip(ratings_count_dict.keys(), isbns):
            if rating_isbn == isbn:
                ratings_counts.append(ratings_count_dict[isbn])

        # Create named tuple to store the data
        Book_data = namedtuple('Book_data', 'isbn title author year avg_rating ratings_count')

        # Create table data to pass through to results template
        table_data = [Book_data(isbn, title, author, year, avg_rating, ratings_count)
                      for isbn, title, author, year, avg_rating, ratings_count, in
                      zip(isbns, titles, authors, years, avg_ratings, ratings_counts)]

    return render_template("search_results.html", table_data=table_data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db.execute("""INSERT INTO "Users" (username, password) VALUES (:username, :password)""",
                   {"username": username, "password": password})
        db.commit()
    return "Registered!"


@app.route("/book", methods=["GET"])
def book():
    "TODO"
