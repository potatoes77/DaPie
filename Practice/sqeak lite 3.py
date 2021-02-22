import sqlite3
import os

conn = sqlite3.connect('example.db')
c = conn.cursor()
print(os.path.exists('example.db'))
print(c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='encouragements' '''))
if c.fetchone()[0]==0:

    #print(os.path.exists('example.db'))
    c.execute('''CREATE TABLE encouragements
             (encouragement text)''')
    c.execute("INSERT INTO encouragements VALUES ('Keep your head up!')")

    conn.commit()
print("BeforeExecute")
c.execute('SELECT * FROM encouragements')
print(c.fetchone())
conn.close()
