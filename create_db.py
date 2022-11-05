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

def db_select(select):
    conn = sqlite3.connect('baza01.db')
    c = conn.cursor()
    c.execute(select)
    data = c.fetchall()
    conn.close()
    return data

def db_insert(insert_data):
    naziv = insert_data[0]
    cena = insert_data[1]
    params = (naziv, cena)
    conn = sqlite3.connect('baza01.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO automobili (id, naziv, cena) VALUES (NULL, ?, ?)", params)
    conn.commit()
    conn.close()

def db_select(params):
    conn = sqlite3.connect('baza01.db')
    c = conn.cursor()
    c.execute(f"SELECT * from automobili")
    data = c.fetchall()
    conn.close()
    return data

#def db_end_conn():
# conn.close()

# commit
# conn.commit()

# close the connection