import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()


def add_encouragements(encouraging_message):
    c.execute(f'''SELECT count(*) FROM encouragements WHERE encouragement='{encouraging_message}' ''')
    if c.fetchone()[0]==0:
        c.execute(f"INSERT INTO encouragements VALUES ('{encouraging_message}')")
        conn.commit()



def get_all_encouragements():
    c.execute('''SELECT * FROM encouragements''')
    rows = c.fetchall()
    return rows

def delete_encouragements(i_will_delete_you):
    c.execute(f'''SELECT count(*) FROM encouragements WHERE encouragement='{i_will_delete_you}' ''')
    if c.fetchone()[0]!=0:
        c.execute(f"DELETE FROM encouragements WHERE encouragement='{i_will_delete_you}'")
        conn.commit()
        return 1
    return 0





add_encouragements("Waddle")
#testTheReturnStatement = delete_encouragements("Waddle")
#print(testTheReturnStatement)
rows = get_all_encouragements()
for row in rows:
    print(row)
conn.close()
