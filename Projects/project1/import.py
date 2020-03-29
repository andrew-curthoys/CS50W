import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Import data from books.csv
with open('books.csv') as f:
    data = csv.reader(f)
    next(data, None)  # skips over the headers
    for isbn, title, author, year in data:
        db.execute("""INSERT INTO "Books" (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)""",
                   {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
