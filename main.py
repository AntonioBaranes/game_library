from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  
    "http://localhost:5500",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class game:
    def __init__(self, title, release_year, genre, console, publisher, img_url=None):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.console = console
        self.publisher = publisher
        self.img_url = img_url

    def __repr__(self):
        return f"Game({self.title}, {self.release_year}, {self.genre}, {self.console}, {self.publisher})"

def get_connection():
    conn = sqlite3.connect('my_games.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

@app.get("/games")
def get_games():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games")
    rows = cursor.fetchall()
    games_list = [game(row['Title'], row['ReleaseYear'], row['Genre'], row['Console'], row['Publisher'],row['img_url']) for row in rows]
    conn.close()
    return games_list

@app.get("/games/snes")
def get_games():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games WhERE Console = 'SNES'")
    rows = cursor.fetchall()
    games_list = [game(row['Title'], row['ReleaseYear'], row['Genre'], row['Console'], row['Publisher'],row['img_url']) for row in rows]
    conn.close()
    return games_list

@app.get("/games/ps1")
def get_games():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games WhERE Console = 'PS1'")
    rows = cursor.fetchall()
    games_list = [game(row['Title'], row['ReleaseYear'], row['Genre'], row['Console'], row['Publisher']) for row in rows]
    conn.close()
    return games_list

@app.get("/games/ps2")
def get_games():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games WhERE Console = 'PS2'")
    rows = cursor.fetchall()
    games_list = [game(row['Title'], row['ReleaseYear'], row['Genre'], row['Console'], row['Publisher']) for row in rows]
    conn.close()
    return games_list

@app.get("/games/n64")
def get_games():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games WhERE Console = 'N64'")
    rows = cursor.fetchall()
    games_list = [game(row['Title'], row['ReleaseYear'], row['Genre'], row['Console'], row['Publisher']) for row in rows]
    conn.close()
    return games_list
