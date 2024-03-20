# # match.py
# import sqlite3

# def create_match_table():
#     conn = sqlite3.connect("sports.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Match (
#         match_id INTEGER PRIMARY KEY,
#         game_date VARCHAR,
#         game_time VARCHAR,
#         team_id INTEGER,
#         FOREIGN KEY (team_id) REFERENCES Team(team_id)
#     );
#     """)
#     conn.commit()
#     conn.close()


