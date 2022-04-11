"""
Initializes oauthecho database.
Author: Thyago Mota
Last Update: April 11, 2022
"""

import sqlite3
import csv
import re

conn = sqlite3.connect('db/oauthecho.db')

# with open('db/oauthecho.sql') as f:
#     conn.executescript(f.read())
# conn.commit()

cursor = conn.cursor()
sql = 'SELECT * FROM access_tokens'
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

conn.close()