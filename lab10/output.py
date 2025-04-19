import psycopg2

# Установление соединения с базой данных
conn = psycopg2.connect(database="postgres", user="postgres", password="8888")
cur = conn.cursor()

# Выполнение SQL-запроса для выборки всех строк из таблицы
cur.execute("SELECT * FROM phonebook")

# Извлечение всех строк
rows = cur.fetchall()

# Вывод всех строк
for row in rows:
    print(row)

# Закрытие соединения
cur.close()
conn.close()
