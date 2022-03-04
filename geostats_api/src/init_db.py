import sqlite3

conn = sqlite3.connect('geostats.db')

with open('sql/geostats.sql') as f:
    conn.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

# cur = conn.cursor()
# cur.execute('SELECT * FROM Regions')

conn.commit()
conn.close()