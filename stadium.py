import sqlite3

def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn

# Function to create the Stadium table with the updated schema
def create_stadium_table(conn):
    cursor = conn.cursor()
    # Drop the existing Stadium table if it exists
    cursor.execute("DROP TABLE IF EXISTS Stadium")
    # Create the Stadium table with the updated schema (without the availability column)
    cursor.execute("""
        CREATE TABLE Stadium (
            stadium_id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            capacity INTEGER
        )
    """)
    conn.commit()
    cursor.close()

def insert_home_stadiums(conn):
    cursor = conn.cursor()
    stadiums_data = [
        ("Old Trafford", "Manchester", 75000),
        ("Anfield", "Liverpool", 54074),
        ("Stamford Bridge", "London", 40834),
        ("Emirates Stadium", "London", 60260),
        ("Etihad Stadium", "Manchester", 55097)
    ]
    cursor.executemany("""
        INSERT INTO Stadium (name, location, capacity) 
        VALUES (?, ?, ?);
    """, stadiums_data)
    conn.commit()
    cursor.close()

conn = connect_to_database("sports.db")
create_stadium_table(conn)
insert_home_stadiums(conn)
