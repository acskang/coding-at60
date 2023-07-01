import sqlite3 as sql3

conn = sql3.connect("db.sqlite3")
cur = conn.cursor()

with open(".pure/people.sql", encoding="UTF-8") as f:
    sql_script = f.read()
    
cur.executescript(sql_script)

cur.close()
conn.close()