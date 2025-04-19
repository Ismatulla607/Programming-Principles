import psycopg2
import csv

conn = psycopg2.connect(database="postgres", user="postgres", password="8888")
cur = conn.cursor()
path = r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab10\LAB10.csv"

# Создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
""")
conn.commit()

# Ввод с консоли
name = input("Введите ваше полное имя: ")
phone = input("Введите ваш номер телефона: ")
cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))
print("Контакт добавлен.")

# Импорт из CSV
with open(path) as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропуск заголовков
    for line in csv_reader:
        cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (line[1], line[2]))
print("Контакты из CSV добавлены.")

# Обновление данных
update = int(input("Хотите обновить данные? (1 - да, 0 - нет): "))
if update == 1:
    old_name = input("Введите старое имя: ")
    new_name = input("Введите новое имя: ")
    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    print("Контакт обновлён.")

# Фильтрация
search = int(input("Хотите найти контакт? (1 - да, 0 - нет): "))
if search == 1:
    filter_mode = int(input("Фильтровать по имени (1) или телефону (0)? "))
    if filter_mode:
        filter_name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (filter_name,))
    else:
        filter_phone = input("Введите номер телефона: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_phone,))
    
    rows = cur.fetchall()
    print("Результаты поиска:")
    for row in rows:
        print(row)

# Удаление
delete = int(input("Хотите удалить контакт? (1 - да, 0 - нет): "))
if delete == 1:
    delete_mode = int(input("Удалить по имени (1) или телефону (0)? "))
    if delete_mode:
        delete_name = input("Введите имя для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (delete_name,))
    else:
        delete_phone = input("Введите номер телефона для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (delete_phone,))
    print("Контакт удалён.")

# Завершение
conn.commit()
cur.close()
conn.close()
    