import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# conn = sqlite3.connect('usersDB.db')
# cursor = conn.cursor()
# create_query = """
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     role TEXT DEFAULT 'user');
#     """
# cursor.execute(create_query)
# conn.commit()
# conn.close()
def connection():
    conn = sqlite3.connect('usersDB.db')
    return conn

def user_data(username, password):
    conn = connection()
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()
            return user
    except sqlite3.Error as e:
        print(f"Обнаружена ошибка: {e}")
        return False
    finally:
        conn.close()


def appendUser(username, password):
    conn = connection()
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            cur_user = cursor.fetchone()
            if cur_user:
                return False
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            return True
    except sqlite3.Error as e:
        print(f"Обнаружена ошибка: {e}")
        return False
    finally:
        conn.close()
def inputLogin():
    username = entry1.get()
    password = entry2.get()
    user_info = user_data(username, password)
    if user_info:
        id, username, password, role = user_info
        messagebox.showinfo("Успех!", f"Добро пожаловать, {username}!\nТвоя роль: {role}. ")

        entry2.delete(0, END)
    else:
        messagebox.showerror("Отказано в доступе.", "Вы не вошли.")

def inputRegister():
    username = entry1.get()
    password = entry2.get()
    if appendUser(username, password):
        messagebox.showinfo("Успех!", "Вы зарегестрировались!")
        entry2.delete(0, END)
    else:
        messagebox.showerror("Упс! Произошла ошибка!.", "Пользователь с таким именем уже существует.")
        entry2.delete(0, END)

def visible(event):
    current = entry2.config()['show'][-1]

    if current == '*':
        entry2.configure(show = '')
        vis.config(text = f"◡", font = "ProunX 14 bold")
    else:
        entry2.configure(show = '*')
        vis.config(text = f"👁", font = "ProunX 12")

app = Tk()
app["bg"] = "#C5D0E6"
app.iconbitmap('auto.ico')
app.title("Авторизация")
app.geometry("300x400")
app.resizable(False, False)
app.geometry("+820+300")

img = PhotoImage(file = "user (1).png")
b = Label(image = img, background = "#C5D0E6")
b.image = img
b.pack(pady = 10)

btn = Button(app, text = "Войти", bg = "#ABCDEF", command = inputLogin)
btn.place(relx = 0.25, rely = 0.25, x = -5, y = 200, width = 160, height = 25)

NewUs = Button(app, text = "Еще не зарегастрированы?", command = inputRegister)
NewUs.pack(side = BOTTOM, pady = 30)

label1 = ttk.Label(text = "login", font = "ProunX 11 bold", background = "#C5D0E6")
label1.place(x = 69, y = 67, width = 150 )
entry1 = ttk.Entry(app)
entry1.place(anchor = CENTER, relx = 0.25, rely = 0.25, x = 70, y = 0,width = 150 )

label2 = ttk.Label(text = "password", font = "ProunX 11 bold", background = "#C5D0E6")
label2.place(x = 69, y = 125,width = 100 )
entry2 = ttk.Entry(app, show = "*")
entry2.place(anchor = CENTER, relx = 0.25, rely = 0.25, x = 70, y = 60,width = 150 )

# visible = Button(app, text = f"👁",bg = "#C5D0E6", command = visible)
vis = ttk.Label(app, text = f"👁", background = "#C5D0E6", font = 12)
vis.place(anchor = CENTER, relx = 0.25, rely = 0.25, x = 160, y = 60,width = 24, height = 24)
vis.bind("<Button-1>", visible)

conn = sqlite3.connect('usersDB.db')

mainloop()
# with conn:
#     cursor = conn.cursor()
#     cursor.execute("UPDATE users SET role = 'admin' WHERE username = 'igor'")