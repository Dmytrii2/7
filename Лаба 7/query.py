import psycopg2

# Параметри підключення
conn = psycopg2.connect(
    host="localhost",
    database="database",
    user="Sydorenko",
    password="1111"
)

cursor = conn.cursor()

# Виконання запиту для вибірки всіх даних з таблиці users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Виведення даних
print("Дані з таблиці users:")
for user in users:
    print(user)

# Закриття курсора і з'єднання
cursor.close()
conn.close()
