import sqlite3

def db_create_table(name):
    conn = sqlite3.connect('baza01.db')
    c = conn.cursor()
    c.execute(f"""CREATE TABLE {name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv TEXT,
            cena REAL)""")
    conn.commit()
    conn.close()

def db_querry(querry, c):
    c.execute(querry)
    data = c.fetchall()
    return data

#def db_end_conn():
# conn.close()

# commit
# conn.commit()

# close the connection