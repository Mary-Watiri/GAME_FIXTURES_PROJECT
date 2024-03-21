import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect("sports.db")
cursor = conn.cursor()

# Create the Team table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Team (
    id INTEGER PRIMARY KEY,
    name TEXT,
    home TEXT,
    availability BOOLEAN
);
""")

# List of football teams to add
football_teams = [
    ("Manchester United", "Old Trafford", 1),  # Home team, available
    ("Liverpool", "Anfield", 1),  # Home team, available
    ("Chelsea", "Stamford Bridge", 1),  # Home team, available
    ("Arsenal", "Emirates Stadium", 0),  # Away team, not available
    ("Manchester City", "Etihad Stadium", 1),  # Home team, available
]

# Insert the football teams into the Team table
cursor.executemany("INSERT INTO Team (name, home, availability) VALUES (?, ?, ?)", football_teams)

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
