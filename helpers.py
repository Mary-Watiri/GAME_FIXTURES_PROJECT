# helpers.py
from __init__ import conn , cursor 
# Function to list all available games
def list_games(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Game")
    games = cursor.fetchall()
    for game in games:
        print(game)
    cursor.close()

# Function to add a new game to the database
def add_game(conn, game_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Game (name) VALUES (?)", (game_name,))
    conn.commit()
    cursor.close()

# Function to list all available stadiums
def list_stadiums(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stadium")
    stadiums = cursor.fetchall()
    for stadium in stadiums:
        print(stadium)
    cursor.close()

# Function to add a new stadium to the database
def add_stadium(conn, stadium_name, location):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Stadium (name, location) VALUES (?, ?)", (stadium_name, location))
    conn.commit()
    cursor.close()

# Function to list all available teams
def list_teams(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Team")
    teams = cursor.fetchall()
    for team in teams:
        print(team)
    cursor.close()

# Function to add a new team to the database
def add_team(conn, team_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Team (name) VALUES (?)", (team_name,))
    conn.commit()
    cursor.close()

# Function to list all players in a specific team or all players across all teams
def list_players(conn, team_id=None):
    cursor = conn.cursor()
    if team_id is None:
        cursor.execute("SELECT * FROM Player")
    else:
        cursor.execute("SELECT * FROM Player WHERE team_id = ?", (team_id,))
    players = cursor.fetchall()
    for player in players:
        print(player)
    cursor.close()

# Function to add a new player to a team
def add_player(conn, player_name, position, team_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Player (name, position, team_id) VALUES (?, ?, ?)", (player_name, position, team_id))
    conn.commit()
    cursor.close()

# Function to list all scheduled game fixtures
def list_fixtures(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GameFixture")
    fixtures = cursor.fetchall()
    for fixture in fixtures:
        print(fixture)
    cursor.close()

# Function to schedule a new game fixture between two teams at a specific stadium and time
def schedule_fixture(conn, game_id, stadium_id, team1_id, team2_id, datetime):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO GameFixture (game_id, stadium_id, team1_id, team2_id, datetime) VALUES (?, ?, ?, ?, ?)", (game_id, stadium_id, team1_id, team2_id, datetime))
    conn.commit()
    cursor.close()
