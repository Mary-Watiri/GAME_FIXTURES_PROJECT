import sqlite3
from tabulate import tabulate

# Establish connection to the SQLite database
def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn

# Function to create the Stadium table with the updated schema
def create_stadium_table(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Stadium")
    cursor.execute("""
        CREATE TABLE Stadium (
            stadium_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            capacity INTEGER,
            availability TEXT  -- New column added
        )
    """)
    conn.commit()
    cursor.close()

# Function to insert predefined home stadiums into the database
def insert_home_stadiums(conn):
    cursor = conn.cursor()
    stadiums_data = [
        ("Old Trafford", "Manchester", 75000, "Available"),
        ("Anfield", "Liverpool", 54074, "Available"),
        ("Stamford Bridge", "London", 40834, "Available"),
        ("Emirates Stadium", "London", 60260, "Available"),
        ("Etihad Stadium", "Manchester", 55097, "Available")
    ]
    cursor.executemany("""
        INSERT INTO Stadium (name, location, capacity, availability) 
        VALUES (?,?,?,?)
    """, stadiums_data)
    conn.commit()
    cursor.close()

# Function to list all available stadiums
def list_stadiums(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stadium")
    stadiums = cursor.fetchall()
    if not stadiums:
        print("No stadiums found.")
    else:
        headers = ["ID", "Name", "Location", "Capacity", "Availability"]  
        print(tabulate(stadiums, headers=headers, tablefmt="grid"))
    cursor.close()

# Function to add a new stadium to the database
def add_stadium(conn, name, location, capacity, availability):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Stadium (name, location, capacity, availability) VALUES (?,?,?,?)",
                   (name, location, capacity, availability))
    conn.commit()
    cursor.close()

# Function to delete a stadium from the database by ID
def delete_stadium(conn, stadium_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Stadium WHERE stadium_id=?", (stadium_id,))
    conn.commit()
    cursor.close()
    print(f"Stadium with ID '{stadium_id}' has been successfully deleted.")

# Function to list all available teams
def list_teams(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Team")
    teams = cursor.fetchall()
    if not teams:
        print("No teams found.")
    else:
        headers = ["ID", "Name", "Home", "Availability"]  
        print(tabulate(teams, headers=headers, tablefmt="grid"))
    cursor.close()

# Function to add a new team to the database
def add_team(conn, team_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Team (name) VALUES (?)", (team_name,))
    conn.commit()
    cursor.close()
    print(f"Team '{team_name}' added successfully.")

# Function to list all players
def list_players(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Player")
    players = cursor.fetchall()
    if not players:
        print("No players found.")
    else:
        headers = [ "Name","age","Position", "Team ID"]
        print(tabulate(players, headers=headers, tablefmt="grid"))
    cursor.close()

# Function to add a new player to a team
def add_player(conn, player_name, position, team_id):
    cursor = conn.cursor()
    # Check if the player already exists in the database
    cursor.execute("SELECT * FROM Player WHERE name =?", (player_name,))
    existing_player = cursor.fetchone()
    if existing_player:
        print(f"Player '{player_name}' already exists in the database.")
        reassign = input("Do you want to reassign the player to a different team? (yes/no): ").lower()
        if reassign == "yes":
            team_id = input("Enter the ID of the new team: ")
        else:
            print("Player assignment canceled.")
            return
    cursor.execute("INSERT INTO Player (name, position, team_id) VALUES (?,?,?)", (player_name, position, team_id))
    conn.commit()
    cursor.close()
    print(f"Player '{player_name}' added successfully.")

# Function to remove a player from the database
def remove_player(conn, player_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Player WHERE id =?", (player_id,))
    conn.commit()
    cursor.close()
    print(f"Player with ID '{player_id}' removed successfully.")

# Function to list all scheduled game fixtures
def list_fixtures(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GameFixture")
    fixtures = cursor.fetchall()
    if not fixtures:
        print("No fixtures found.")
    else:
        headers = ["Date", "Time", "Venue", "Match ID", "Team 1 ID", "Team 2 ID", "Teams Playing"]
        print(tabulate(fixtures, headers=headers, tablefmt="grid"))
    cursor.close()

# Function to delete a team from the database
def delete_team(conn, team_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Team WHERE ID=?", (team_id,))
    conn.commit()
    cursor.close()
    print(f"Team with ID '{team_id}' has been successfully deleted.")

def is_venue_available(conn, game_venue, game_date, game_time):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GameFixture WHERE game_venue = ? AND game_date = ? AND game_time = ?", (game_venue, game_date, game_time))
    existing_match = cursor.fetchone()
    cursor.close()
    return existing_match is None

def schedule_fixture(conn, game_date, game_time, game_venue, match_id, team1_id, team2_id):
    cursor = conn.cursor()

    # Check if match ID already exists
    cursor.execute("SELECT * FROM GameFixture WHERE match_id = ?", (match_id,))
    existing_match = cursor.fetchone()
    if existing_match:
        print(f"Error: Match with ID {match_id} already exists.")
        cursor.close()
        return

    # Check if both teams exist
    cursor.execute("SELECT name FROM Team WHERE ID = ?", (team1_id,))
    team1_row = cursor.fetchone()
    cursor.execute("SELECT name FROM Team WHERE ID = ?", (team2_id,))
    team2_row = cursor.fetchone()

    if not team1_row:
        print(f"Error: Team with ID {team1_id} does not exist.")
        cursor.close()
        return
    if not team2_row:
        print(f"Error: Team with ID {team2_id} does not exist.")
        cursor.close()
        return

    # Fetch team names
    team1_name = team1_row[0]
    team2_name = team2_row[0]

    # Check if the venue is available
    if not is_venue_available(conn, game_venue, game_date, game_time):
        print(f"Error: Venue {game_venue} is not available on {game_date} at {game_time}.")
        cursor.close()
        return

    # Insert fixture into the database
    try:
        cursor.execute("""
            INSERT INTO GameFixture (game_date, game_time, game_venue, match_id, team1_id, team2_id, teams_playing)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (game_date, game_time, game_venue, match_id, team1_id, team2_id, f"{team1_name} vs {team2_name}"))
        conn.commit()
        print(f"Fixture with match ID '{match_id}' has been successfully scheduled at venue '{game_venue}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
def cancel_fixture(conn, match_id):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM GameFixture WHERE match_id = ?", (match_id,))
        conn.commit()
        print(f"Fixture with match ID '{match_id}' has been successfully canceled.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()