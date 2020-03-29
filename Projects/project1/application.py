import os
import requests
from dotenv import load_dotenv
from collections import namedtuple

from flask import Flask, session, render_template, request, jsonify
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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if session["username"] is None:
            return render_template("index.html")
        else:
            return  render_template("search.html")

    if request.method == "POST":
        # Check that a username & password has been entered
        if not request.form.get("username") or not request.form.get("password"):
            error_message = "Please provide a username and password"
            return render_template("error.html", error_message=error_message)

        # Get username & password and check against database
        username = request.form.get("username")
        password = request.form.get("password")
        login_data = db.execute("""SELECT * from "Users" WHERE username = :username""",
                                {"username": username}).fetchone()

        # Check that username/password match an entry in the database
        if login_data is None :
            error_message = "Username not found, please retry"
            return render_template("error.html", error_message=error_message)

        # Check password against database
        db_password = login_data[2]
        if password != db_password:
            error_message = "Incorrect password, please retry"
            return render_template("error.html", error_message=error_message)

        # Set session variables
        session["username"] = username
        session["user_id"] = login_data[0]

        return render_template("/search.html")


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


@app.route("/book", methods=["GET", "POST"])
def book():
    isbn = request.args.get("isbn")
    user_id = session["user_id"]
    review_data = db.execute("""SELECT * FROM "Reviews" WHERE user_id = :user_id AND isbn = :isbn""",
                             {"user_id": user_id, "isbn": isbn}).fetchone()

    book_data = db.execute("""SELECT * FROM "Books" WHERE isbn = :isbn""",
                           {"isbn": isbn}).fetchone()

    if review_data is None:
        review_stars = "-"
        review_comment = "No user review yet"

    else:
        # Get user review data
        review_stars = review_data[2]
        review_comment = review_data[3]

    # Get book data
    isbn = book_data[0]
    title = book_data[1]
    author = book_data[2]
    year = book_data[3]

    # Get reviews from Goodreads
    load_dotenv(override=True)
    KEY = os.getenv('key')
    url = 'https://www.goodreads.com/book/review_counts.json'
    params = {"key": KEY, "isbns": isbn}
    response = requests.get(url, params=params)
    goodreads_data = response.json()

    # Parse data from Goodreads into lists to pass to results template
    avg_rating = goodreads_data.get('books')[0].get('average_rating')
    ratings_count = goodreads_data.get('books')[0].get('work_ratings_count')

    if request.method == "GET":
        if review_data is None:
            return render_template("/review.html", title=title, author=author, year=year, avg_rating=avg_rating, ratings_count=ratings_count, review_stars=review_stars, review_comment=review_comment, isbn=isbn)
        else:
            return render_template("/book.html", title=title, author=author, year=year, avg_rating=avg_rating, ratings_count=ratings_count, review_stars=review_stars, review_comment=review_comment, isbn=isbn)

    if request.method == "POST":
        stars = request.form.get("stars")
        comment = request.form.get("comment")
        db.execute("""INSERT INTO "Reviews" (user_id, isbn, stars, comment) VALUES (:user_id, :isbn, :stars, :comment)""",
                   {"user_id": user_id, "isbn": isbn, "stars": stars, "comment": comment})
        db.commit()

        return render_template("/book.html", title=title, author=author, year=year, avg_rating=avg_rating, ratings_count=ratings_count, review_stars=review_stars, review_comment=review_comment, isbn=isbn)


@app.route("/api/<isbn>", methods=["GET"])
def api(isbn):
    # Get book information
    book_data = db.execute("""SELECT * FROM "Books" WHERE isbn = :isbn""",
                           {"isbn": isbn}).fetchone()

    # Get reviews from Goodreads
    load_dotenv(override=True)
    KEY = os.getenv('key')
    url = 'https://www.goodreads.com/book/review_counts.json'
    params = {"key": KEY, "isbns": isbn}
    response = requests.get(url, params=params)
    goodreads_data = response.json()

    # Assign variables
    title = book_data[1]
    author = book_data[2]
    year = book_data[3]
    isbn = book_data[0]
    review_count = goodreads_data.get('books')[0].get('work_ratings_count')
    avg_score = goodreads_data.get('books')[0].get('average_rating')

    return jsonify({
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "review_count": review_count,
        "average_score": avg_score
    })


@app.route("/logout", methods=["GET"])
def logout():
    session['username'] = None
    return render_template("/logout.html")

