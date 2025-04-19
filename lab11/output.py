import psycopg2


conn = psycopg2.connect(database="postgres", user="postgres", password="8888")
cur = conn.cursor()

cur.execute("SELECT * FROM phonebook2")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()