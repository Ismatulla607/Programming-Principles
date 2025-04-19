import psycopg2

conn = psycopg2.connect(
    database="postgres", 
    user="postgres",
    host="localhost",
    password="8888",
    port=5432
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS LAB11 (
        id SERIAL PRIMARY KEY,
        names VARCHAR(30),
        phone VARCHAR(20)
    );
""")

conn.commit()
cur.close()
conn.close()
