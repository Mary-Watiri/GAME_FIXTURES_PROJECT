# helpers.py

import sqlite3

# Establish connection to the SQLite database
def connect_to_database(database_file):
    conn = sqlite3.connect(database_file)
    return conn

# Function to list all available stadiums
def list_stadiums():
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stadium")
    stadiums = cursor.fetchall()
    for stadium in stadiums:
        print(stadium)
    cursor.close()

# Function to add a new stadium to the database
def add_stadium(stadium_name, location):
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Stadium (name, location) VALUES (?, ?)", (stadium_name, location))
    conn.commit()
    cursor.close()

# Function to list all available teams
def list_teams():
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Team")
    teams = cursor.fetchall()
    for team in teams:
        print(team)
    cursor.close()

# Function to add a new team to the database
def add_team(team_name):
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Team (name) VALUES (?)", (team_name,))
    conn.commit()
    cursor.close()

# Function to list all players
def list_players():
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Player")
    players = cursor.fetchall()
    for player in players:
        print(player)
    cursor.close()

# helpers.py

# Function to add a new player to a team
def add_player(conn, player_name, position, team_id):
    cursor = conn.cursor()
    # Check if the player already exists in the database
    cursor.execute("SELECT * FROM Player WHERE name = ?", (player_name,))
    existing_player = cursor.fetchone()
    if existing_player:
        print(f"Player '{player_name}' already exists in the database.")
        reassign = input("Do you want to reassign the player to a different team? (yes/no): ").lower()
        if reassign == "yes":
            team_id = input("Enter the ID of the new team: ")
        else:
            print("Player assignment canceled.")
            return
    cursor.execute("INSERT INTO Player (name, position, team_id) VALUES (?, ?, ?)", (player_name, position, team_id))
    conn.commit()
    cursor.close()


# Function to list all scheduled game fixtures
def list_fixtures():
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GameFixture")
    fixtures = cursor.fetchall()
    for fixture in fixtures:
        print(fixture)
    cursor.close()

# Function to schedule a new game fixture between two teams
def schedule_fixture(game_date, game_time, game_venue, match_id, team1_id, team2_id):
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO GameFixture (game_date, game_time, game_venue, match_id, team1_id, team2_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (game_date, game_time, game_venue, match_id, team1_id, team2_id))
    conn.commit()
    cursor.close()

# Function to cancel a scheduled game fixture
def cancel_fixture(match_id):
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GameFixture WHERE match_id = ?", (match_id,))
    conn.commit()
    cursor.close()

# Function to remove a player from the database
def remove_player(player_id):
    conn = connect_to_database("sports.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Player WHERE id = ?", (player_id,))
    conn.commit()
    cursor.close()
