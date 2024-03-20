# import sqlite3

# def create_coach_table():
#     conn = sqlite3.connect("sports.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Coach (
#         coach_id INTEGER PRIMARY KEY,
#         coach_name TEXT
#     );
#     """)
#     conn.commit()
    
#     cursor.execute("INSERT INTO Coach (coach_name) VALUES ('Mikel Arteta')")
#     conn.commit()

#     conn.close()

# create_coach_table()
