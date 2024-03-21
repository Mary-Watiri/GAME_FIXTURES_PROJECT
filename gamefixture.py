import sqlite3

# Function to establish a connection to the SQLite database
def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn

# Function to create the GameFixture table if it doesn't exist
def create_game_fixture_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS GameFixture (
            fixture_id INTEGER PRIMARY KEY,
            game_date TEXT,
            game_time TEXT,
            game_venue TEXT,
            match_id INTEGER,
            team1_id INTEGER,
            team2_id INTEGER,
            teams_playing TEXT,
            UNIQUE (match_id, team1_id, team2_id),
            FOREIGN KEY (match_id) REFERENCES Match(match_id),
            FOREIGN KEY (team1_id) REFERENCES Team(id),
            FOREIGN KEY (team2_id) REFERENCES Team(id)
        );
    """)
    conn.commit()
    cursor.close()

# Function to insert a new game fixture into the database
def insert_game_fixture(conn, game_date, game_time, game_venue, match_id, team_id1, team_id2):
    cursor = conn.cursor()
    # Fetch team names dynamically using the provided team IDs
    team1_name = cursor.execute("SELECT name FROM Team WHERE id = ?", (team_id1,)).fetchone()[0]
    team2_name = cursor.execute("SELECT name FROM Team WHERE id = ?", (team_id2,)).fetchone()[0]
    fixture_description = f"{team1_name} vs {team2_name}"
    cursor.execute("""
        INSERT INTO GameFixture (game_date, game_time, game_venue, match_id, team1_id, team2_id, teams_playing)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (game_date, game_time, game_venue, match_id, team_id1, team_id2, fixture_description))
    conn.commit()
    cursor.close()

# Establish a connection to the SQLite database
conn = connect_to_database("sports.db")

# Create the GameFixture table if it doesn't exist
create_game_fixture_table(conn)

# Insert a new game fixture into the database
insert_game_fixture(conn, "2024-04-01", "15:00", "Stadium A", 1, 1, 2)
