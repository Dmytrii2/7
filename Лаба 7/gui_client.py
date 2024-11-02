import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import messagebox
import psycopg2

# Підключення до бази даних
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="database",
            user="Sydorenko",
            password="1111"
        )
        return conn
    except psycopg2.OperationalError as e:
        messagebox.showerror("Помилка підключення", f"Не вдалося підключитися до бази даних: {e}")
        return None

# Функція для завантаження даних з БД
def load_data():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        # Очищення таблиці перед завантаженням нових даних
        for row in table.get_children():
            table.delete(row)
        # Додавання даних у таблицю
        for row in rows:
            table.insert("", "end", values=row)
        cursor.close()
        conn.close()

# Функція для додавання нового користувача
def add_user():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        username = entry_username.get()
        email = entry_email.get()
        try:
            cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
            conn.commit()
            load_data()  # Оновлення даних у таблиці
            entry_username.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            messagebox.showinfo("Успішно", "Користувача додано")
        except psycopg2.Error as e:
            messagebox.showerror("Помилка SQL", f"Не вдалося додати користувача: {e}")
        cursor.close()
        conn.close()

# Налаштування графічного інтерфейсу
root = tk.Tk()
root.title("Графічний клієнт для управління БД")
root.geometry("400x300")

# Віджети для введення даних
tk.Label(root, text="Ім'я користувача:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для додавання користувача
btn_add = tk.Button(root, text="Додати користувача", command=add_user)
btn_add.grid(row=2, column=1, padx=10, pady=10)

# Таблиця для відображення користувачів
table = tk.ttk.Treeview(root, columns=("ID", "Username", "Email"), show="headings")
table.heading("ID", text="ID")
table.heading("Username", text="Ім'я користувача")
table.heading("Email", text="Email")
table.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Кнопка для завантаження даних з БД
btn_load = tk.Button(root, text="Завантажити дані", command=load_data)
btn_load.grid(row=4, column=1, padx=10, pady=10)

# Запуск програми
root.mainloop()
