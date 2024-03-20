# import sqlite3
# class Players:
#     def __init__(self, db_path="sports.db"):
#         self.conn = sqlite3.connect(db_path)
#         self.cursor = self.conn.cursor()

#     def add_player(self, player_name, coach_id, team_id):
#         """
#         Adds a player to the Players table.
#         :param player_name: Name of the player
#         :param coach_id: ID of the coach associated with the player
#         :param team_id: ID of the team the player belongs to
#         """
#         try:
#             # Check if the player already belongs to a team
#             existing_team_id = self.get_team_id_for_player(player_name)
#             if existing_team_id:
#                 print(f"{player_name} already belongs to Team {existing_team_id}.")
#                 return

#             # Insert the player into the Players table
#             self.cursor.execute("""
#                 INSERT INTO Players (player_name, coach_id, team_id)
#                 VALUES (?, ?, ?)
#             """, (player_name, coach_id, team_id))
#             self.conn.commit()
#             print(f"{player_name} added successfully to Team {team_id}.")
#         except sqlite3.Error as e:
#             print(f"Error adding player: {e}")
#         finally:
#             self.close_connection()

#     def get_team_id_for_player(self, player_name):
#         """
#         Retrieves the team ID for a given player.
#         :param player_name: Name of the player
#         :return: Team ID (or None if player not found)
#         """
#         try:
#             self.cursor.execute("""
#                 SELECT team_id FROM Players WHERE player_name = ?
#             """, (player_name,))
#             result = self.cursor.fetchone()
#             return result[0] if result else None
#         except sqlite3.Error as e:
#             print(f"Error retrieving team ID for player: {e}")
#         finally:
#             self.close_connection()

#     def close_connection(self):
#         """
#         Closes the database connection.
#         """
#         self.conn.close()

# # Example usage:
# if __name__ == "__main__":
#     players_db = Players()
#     players_db.add_player("John Doe", coach_id=1, team_id=101)
#     players_db.add_player("Jane Smith", coach_id=2, team_id=102)
