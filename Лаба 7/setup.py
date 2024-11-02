import psycopg2
from faker import Faker

# Параметри підключення
conn = psycopg2.connect(
    host="localhost",
    database="database",
    user="Sydorenko",
    password="1111"
)

cursor = conn.cursor()

# Видалення таблиці, якщо вона існує
cursor.execute('DROP TABLE IF EXISTS users;')

# Створення таблиці
cursor.execute('''
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
''')

# Генерація даних за допомогою Faker
fake = Faker()
for _ in range(10):  # Згенеруйте 10 користувачів
    cursor.execute('''
        INSERT INTO users (name, email) VALUES (%s, %s)
    ''', (fake.name(), fake.email()))

conn.commit()  # Застосувати зміни

# Закриття курсора і з'єднання
cursor.close()
conn.close()
