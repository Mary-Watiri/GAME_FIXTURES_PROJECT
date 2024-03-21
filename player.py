import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect("sports.db")
cursor = conn.cursor()

# Create Player table with name, age, position, and team_id columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS Player (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    position TEXT,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES Team(id)
);
""")

# List of player data including name, age, position, and team_id
players_data = [
    ("Lionel Messi", 34, "Forward", 1),
    ("Cristiano Ronaldo", 36, "Forward", 2),
    ("Neymar Jr.", 29, "Forward", 3),
    ("Kylian Mbappe", 23, "Forward", 4),
    ("Robert Lewandowski", 33, "Forward", 5),
    ("Kevin De Bruyne", 30, "Midfielder", 1),
    ("Virgil van Dijk", 30, "Defender", 2),
    ("Mohamed Salah", 29, "Forward", 3),
    ("Sadio Mane", 29, "Forward", 4),
    ("Harry Kane", 28, "Forward", 5),
    ("Raheem Sterling", 27, "Forward", 1),
    ("Sergio Ramos", 35, "Defender", 2),
    ("Sergio Aguero", 33, "Forward", 3),
    ("Luka Modric", 36, "Midfielder", 4),
    ("Karim Benzema", 33, "Forward", 5),
    ("Manuel Neuer", 35, "Goalkeeper", 1),
    ("Eden Hazard", 30, "Forward", 2),
    ("Paul Pogba", 28, "Midfielder", 3),
    ("Antoine Griezmann", 30, "Forward", 4),
    ("Toni Kroos", 31, "Midfielder", 5)
]

# Insert players into the database
for player_data in players_data:
    cursor.execute("INSERT INTO Player (name, age, position, team_id) VALUES (?, ?, ?, ?)", player_data)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
