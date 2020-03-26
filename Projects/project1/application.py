import os
import requests
from dotenv import load_dotenv

from flask import Flask, session
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

    return "TODO"

@app.route("/search")
def search():
    load_dotenv(override=True)
    KEY = os.getenv('key')
    url = 'https://www.goodreads.com/book/review_counts.json'
    params = {"key": KEY, "isbns": "9781632168146"}
    response = requests.get(url, params=params)