# # team.py
# import sqlite3

# def create_team_table():
#     conn = sqlite3.connect("sports.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Team (
#         team_id INTEGER PRIMARY KEY,
#         team_name TEXT,
#         coach_id INTEGER,
#         FOREIGN KEY (coach_id) REFERENCES Coach(coach_id)
#     );
#     """)
#     conn.commit()
#     conn.close()


