import sqlite3

class GameFixtures:
    def __init__(self, db_name="sports.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Create GameFixtures table if not exists
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GameFixtures (
            fixture_id INTEGER PRIMARY KEY,
            game_date VARCHAR,
            game_time VARCHAR,
            game_venue TEXT,
            match_id INTEGER,
            team_id INTEGER,
            team_selected BOOLEAN DEFAULT 0,
            UNIQUE (match_id, team_id),
            FOREIGN KEY (match_id) REFERENCES Match(match_id),
            FOREIGN KEY (team_id) REFERENCES Team(team_id)
        );
        """)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def is_team_selected(self, match_id, team_id):
        """Check if a team is already selected for a match."""
        self.cursor.execute("SELECT COUNT(*) FROM GameFixtures WHERE match_id = ? AND team_id = ?", (match_id, team_id))
        count = self.cursor.fetchone()[0]
        return count > 0

    def is_venue_available(self, game_date, game_time, game_venue):
        """Check if a venue is available at a specific time."""
        self.cursor.execute("SELECT COUNT(*) FROM GameFixtures WHERE game_date = ? AND game_time = ? AND game_venue = ?", 
                        (game_date, game_time, game_venue))
        count = self.cursor.fetchone()[0]
        return count == 0

    def create_game_fixture(self, game_date, game_time, game_venue, match_id, team_id1, team_id2):
        """Insert a game fixture between two teams into the database, ensuring constraints."""
        if team_id1 == team_id2:
           print("Error: Teams cannot play against themselves.")
           return False

        if self.is_team_selected(match_id, team_id1) or self.is_team_selected(match_id, team_id2):
           print("Error: One or both teams already selected for this match.")
           return False

        if not self.is_venue_available(game_date, game_time, game_venue):
           print("Error: Venue already occupied at this time.")
           return False

    # Fetch team names based on team IDs
        self.cursor.execute("SELECT team_name FROM Team WHERE team_id = ?", (team_id1,))
        team1_name = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT team_name FROM Team WHERE team_id = ?", (team_id2,))
        team2_name = self.cursor.fetchone()[0]

    # Concatenate team names with "vs" term
        teams_playing = f"{team1_name} vs {team2_name}"

        self.cursor.execute("""
        INSERT INTO GameFixtures (game_date, game_time, game_venue, match_id, team_id)
        VALUES (?, ?, ?, ?, ?)
    """, (game_date, game_time, game_venue, match_id, teams_playing))
    
        self.conn.commit()
        print("Game fixture created successfully.")
        return True
