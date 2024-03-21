import sqlite3


def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn


def create_stadium_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stadium (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            capacity INTEGER,
            available BOOLEAN
        );
    """)
    conn.commit()
    cursor.close()


def insert_home_stadiums(conn):
    cursor = conn.cursor()
    stadiums_data = [
        ("Old Trafford", "Manchester", 75000, True),
        ("Anfield", "Liverpool", 54074, True),
        ("Stamford Bridge", "London", 40834, True),
        ("Emirates Stadium", "London", 60260, True),
        ("Etihad Stadium", "Manchester", 55097, True)
    ]
    cursor.executemany("""
        INSERT INTO Stadium (name, location, capacity, available) 
        VALUES (?, ?, ?, ?);
    """, stadiums_data)
    conn.commit()
    cursor.close()


conn = connect_to_database("sports.db")
create_stadium_table(conn)
insert_home_stadiums(conn)
