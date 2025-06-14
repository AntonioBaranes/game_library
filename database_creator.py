
import pandas as pd

import sqlite3

def print_all_games():
    conn = sqlite3.connect('my_games.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def insert_img_url(game_title, img_url):
    conn = sqlite3.connect('my_games.db')
    cursor = conn.cursor()
    query = ('''
    UPDATE games
    SET img_url = ?
    WHERE title = ?;
    ''',
    (img_url, game_title))
    
    cursor.execute(*query)
    conn.commit()
    conn.close()


# insert_img_url("Chrono Trigger", 'https://i.etsystatic.com/12175780/r/il/45cb26/5797700079/il_fullxfull.5797700079_es12.jpg')
# insert_img_url("Final Fantasy VI", 'https://m.media-amazon.com/images/M/MV5BNjY1NzY1N2ItZjczMy00YjM1LTk0ZDMtODFiOTMyMzczNTIyXkEyXkFqcGc@._V1_QL75_UX190_CR0,2,190,281_.jpg')
# insert_img_url("Super Metroid",'https://i.etsystatic.com/37268737/r/il/6d9c03/4184016158/il_fullxfull.4184016158_rsks.jpg')
insert_img_url("Megaman X", 'https://m.media-amazon.com/images/I/71RKjZUwdRS._AC_UF894,1000_QL80_.jpg')
print_all_games()

# insert_img_url("The Legend of Zelda: A Link to the Past", 'https://m.media-amazon.com/images/M/MV5BN2U5OWRiMWYtMmI1Mi00MDMyLWFkOTctYTI3ZmYyMDk2ZTkzXkEyXkFqcGc@._V1_QL75_UX145_.jpg')
#print_all_games()

# def execute_script(script, conn):
#     try:
#         with conn:
#             conn.executescript(script)
#             print("Script executed successfully.")
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")

# conn = sqlite3.connect('my_games.db')
# cursor = conn.cursor()

# #Use this varibale to write the querries to add things to the database
# script_table_create = '''
# CREATE TABLE IF NOT EXISTS Publishers (
#     Name Text Primary Key,
#     Country text
# );'''

# script_add_values = '''
# INSERT INTO Publishers (Name, Country) VALUES
# ('Nintendo', 'Japan'),
# ('Sony', 'Japan'),
# ('Microsoft', 'USA'),
# ('Electronic Arts', 'USA'),
# ('Activision Blizzard', 'USA'),
# ('Ubisoft', 'France'),
# ('Bandai Namco Entertainment', 'Japan'),
# ('Sega', 'Japan'),
# ('Capcom', 'Japan'),
# ('Square Enix', 'Japan');
# '''

# create_games_table = '''
# Create Table IF NOT EXISTS Games (
#     Title Text Primary Key,
#     ReleaseYear Integer,
#     Genre Text,
#     Console Text References Consoles(Name),
#     Publisher Text References Publishers(Name));
# '''

# insert_games_snes = '''
# INSERT INTO Games (Title, ReleaseYear, Genre, Console, Publisher) VALUES
# ('Super Mario World', 1990, 'Platformer', 'SNES', 'Nintendo'),
# ('The Legend of Zelda: A Link to the Past', 1991, 'Action-adventure', 'SNES', 'Nintendo'),
# ('Chrono Trigger', 1995, 'JRPG', 'SNES', 'Square Enix'),
# ('Final Fantasy VI', 1994, 'JRPG', 'SNES', 'Square Enix'),
# ('Super Metroid', 1994, 'MetroidVania', 'SNES', 'Nintendo'),
# ('Megaman X', 1993, 'Platformer', 'SNES', 'Capcom');
# '''

# insert_games_n64 = '''
# INSERT INTO Games (Title, ReleaseYear, Genre, Console, Publisher) VALUES
# ('Super Mario 64', 1996, 'Platformer', 'N64', 'Nintendo'),
# ('The Legend of Zelda: Ocarina of Time', 1998, 'Action-adventure', 'N64', 'Nintendo'),
# ("The Legend of Zelda: Majora's Mask", 2000, 'Action-adventure', 'N64', 'Nintendo'),
# ('Super Smash Bros.', 1999, 'Fighting', 'N64', 'Nintendo'),
# ('Star Wars: shadow of the Empire', 1996, 'Action-adventure', 'N64', 'LucasArts');
# '''

# insert_games_ps1 = '''
# INSERT INTO Games (Title, ReleaseYear, Genre, Console, Publisher) VALUES
# ('Final Fantasy VII', 1997, 'JRPG', 'PS1', 'Square Enix'),
# ('Metal Gear Solid', 1998, 'Action-adventure', 'PS1', 'Konami'),
# ('Castlevania: Symphony of the Night', 1997, 'MetroidVania', 'PS1', 'Konami'),
# ('Resident Evil 2', 1998, 'Survival Horror', 'PS1', 'Capcom'),
# ('Resident Evil 3: Nemesis', 1999, 'Survival Horror', 'PS1', 'Capcom');
# '''

# insert_games_ps2 = '''
# Insert INTO Games (Title, ReleaseYear, Genre, Console, Publisher) VALUES
# ('Grand Theft Auto: San Andreas', 2004, 'Action-adventure', 'PS2', 'Rockstar Games'),
# ('Final Fantasy X', 2001, 'JRPG', 'PS2', 'Square Enix'),
# ('Resident Evil 4', 2005, 'Survival Horror', 'PS2', 'Capcom'),
# ('God of War', 2005, 'Hack and Slash', 'PS2', 'Sony'),
# ('Kingdom Hearts', 2002, 'Action RPG', 'PS2', 'Square Enix'),
# ('Persona 4', 2008, 'JRPG', 'PS2', 'Atlus'),
# ('Persona 3 FES', 2007, 'JRPG', 'PS2', 'Atlus'),
# ('Madden NFL 2007', 2006, 'Sports', 'PS2', 'Electronic Arts'),
# ('Madden NFL 2008', 2007, 'Sports', 'PS2', 'Electronic Arts'),
# ('Kingdom Hearts II', 2005, 'Action RPG', 'PS2', 'Square Enix'),
# ('Metal Gear Solid 3: Snake Eater', 2004, 'Action-adventure', 'PS2', 'Konami'),
# ('Grand Theft Auto: Vice City', 2002, 'Action-adventure', 'PS2', 'Rockstar Games'),
# ('Grand Theft Auto III', 2001, 'Action-adventure', 'PS2', 'Rockstar Games'),
# ('Devil May Cry', 2001, 'Hack and Slash', 'PS2', 'Capcom'),
# ("Devil May Cry 3: Dante's Awakening", 2005, 'Hack and Slash', 'PS2', 'Capcom'),
# ("Devil May Cry 2", 2003, 'Hack and Slash', 'PS2', 'Capcom'),
# ("God of War II", 2007, 'Hack and Slash', 'PS2', 'Sony'),
# ("Battlefront 2", 2005, 'Action-adventure', 'PS2', 'LucasArts');
# '''

# execute_script(insert_games_ps2, conn)

# print(pd.read_sql_query("SELECT * FROM Games", conn))

# conn.close()
# conn = sqlite3.connect('my_games.db')
# cursor = conn.cursor()
# cursor.execute('''
# ALTER TABLE games
# ADD COLUMN img_url TEXT;''')
# conn.commit()

# cursor.execute('''UPDATE games
#                SET img_url = 'https://m.media-amazon.com/images/M/MV5BZjZkZWVjNTYtZDMzZC00N2YxLTg2NjUtMTdlMzJiMDk3MTNhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg'
#                WHERE title = 'Super Mario World';''')
# conn.commit();

