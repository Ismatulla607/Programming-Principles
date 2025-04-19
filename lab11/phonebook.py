import psycopg2
import re

def connect_db():
    return psycopg2.connect(database="postgres", user="postgres", password="8888")

def create_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)

def is_valid_phone(phone):
    return re.match(r'^8\d{10}$', phone) is not None

def add_or_update_user(cur, name, phone):
    if not is_valid_phone(phone):
        print("Неверный формат номера. Он должен начинаться с 8 и содержать 11 цифр.")
        return
    cur.execute("SELECT * FROM phonebook2 WHERE name = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook2 SET phone = %s WHERE name = %s", (phone, name))
        print("Контакт обновлён.")
    else:
        cur.execute("INSERT INTO phonebook2(name, phone) VALUES (%s, %s)", (name, phone))
        print("Контакт добавлен.")

def search_by_pattern(cur, pattern):
    query = """
        SELECT * FROM phonebook2
        WHERE name ILIKE %s OR phone LIKE %s;
    """
    cur.execute(query, (f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    if rows:
        print("Найденные контакты:")
        for row in rows:
            print(row)
    else:
        print("Контакты не найдены.")

def get_all_paginated(cur, limit, offset):
    cur.execute("SELECT * FROM phonebook2 ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    print("Контакты (страница):")
    for row in rows:
        print(row)

def delete_user(cur, name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook2 WHERE name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook2 WHERE phone = %s", (phone,))
    else:
        print("Не указаны данные для удаления.")
        return
    print("Контакт удалён.")

def main():
    conn = connect_db()
    cur = conn.cursor()
    create_table(cur)

    while True:
        print("\nВыберите действие:")
        print("1. Поиск по шаблону (имя или номер)")
        print("2. Добавить или обновить контакт")
        print("3. Показать список с пагинацией")
        print("4. Удалить контакт")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            pattern = input("Введите шаблон для поиска: ")
            search_by_pattern(cur, pattern)

        elif choice == "2":
            name = input("Введите имя: ")
            phone = input("Введите номер: ")
            add_or_update_user(cur, name, phone)

        elif choice == "3":
            limit = int(input("Лимит: "))
            offset = int(input("Смещение: "))
            get_all_paginated(cur, limit, offset)

        elif choice == "4":
            mode = input("Удалить по имени (1) или по номеру (0)? ")
            if mode == "1":
                name = input("Имя: ")
                delete_user(cur, name=name)
            else:
                phone = input("Телефон: ")
                delete_user(cur, phone=phone)

        elif choice == "5":
            break
        else:
            print("Неверный выбор.")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
