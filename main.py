# import tkinter as tk
# from tkinter import ttk
# import sqlite3

# # Класс главного окна
# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.init_main()
#         self.db = db
#         self.view_records()

# ####################################################
#     ## Создание и работа с главным окном
#     def init_main(self):
#         toolbar = tk.Frame(bg = '#d7d7d7', bd = 2)
#         toolbar.pack(side = tk.TOP, fill = tk.X)
# #################################################### КНОПКИ
#         # ДОБАВИТЬ
#         self.add_img = tk.PhotoImage(file='./img/add.png')
#         btn_add = tk.Button(toolbar, bg='#d7d7d7', bd = 1,
#                             image = self.add_img, command = self.open_child)
#         btn_add.pack(side = tk.LEFT)
# #################################################### СОЗДАНИЕ ТАБЛИЦЫ 

#         # Добавляем столбцы
#         self.tree = ttk.Treeview(self, columns = ('ID', 'name', 'phone', 'email'),
#                                  height = 45, show = 'headings')
        
#         # Добавить параметры колонкам
#         self.tree.column('ID', width = 45, anchor = tk.CENTER)
#         self.tree.column('name', width = 300, anchor = tk.CENTER)
#         self.tree.column('phone', width = 150, anchor = tk.CENTER)
#         self.tree.column('email', width = 150, anchor = tk.CENTER)

#         # Подписи колонок
#         self.tree.heading('ID', text = 'ID')
#         self.tree.heading('name', text = 'ФИО')
#         self.tree.heading('phone', text = 'Телефон')
#         self.tree.heading('email', text = 'E-mail')

#         # Упаковка
#         self.tree.pack(side = tk.LEFT)
# #################################################### ВСЕ МЕТОДЫ

#     def records(self, name, phone, email):
#         self.db.insert_data(name, phone, email)
#         self.view_records()

#     def view_records(self):
#         self.db.cur.execute(''' SELECT * FROM users ''')

#         [self.tree.delete(i) for i in self.tree.get_children()]
#         [self.tree.insert('', 'end', values = row)
#          for row in self.db.cur.fetchall()]

# #################################################### ВЫЗОВ КЛАССОВ
#     # Метод вызывающий окно добавления
#     def open_child(self):
#         Child()


# ####################################################
# # Дочернее окно
# class Child(tk.Toplevel):
#     def __init__(self):
#         super().__init__(root)
#         self.init_child()
#         self.view = app

#     def init_child(self):
#         self.title('Добавить контакт')
#         self.geometry('400x220')
#         self.resizable(False, False)
#         self.grab_set()
#         self.focus_set()
# ####################################################
#         label_name = tk.Label(self, text = 'ФИО: ')
#         label_name.place(x = 50, y = 50)
#         label_phone = tk.Label(self, text = 'Телефон: ')
#         label_phone.place(x = 50, y = 80)
#         label_email = tk.Label(self, text = 'E-mail: ')
#         label_email.place(x = 50, y = 110)

#         self.entry_name = ttk.Entry(self)
#         self.entry_name.place(x = 200, y = 50)
#         self.entry_phone = ttk.Entry(self)
#         self.entry_phone.place(x = 200, y = 80)
#         self.entry_email = ttk.Entry(self)
#         self.entry_email.place(x = 200, y = 110)
# ####################################################
#         # кнопка закрытия 
#         self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
#         self.btn_cancel.place(x = 300, y = 170)

#         # Кнопка добавления
#         self.btn_add = ttk.Button(self, text = 'Добавить')
#         self.btn_add.place(x = 220, y = 170)
#         self.btn_add.bind('<Button-1>', lambda event:
#                           self.view.records(self.entry_name.get(),
#                                             self.entry_phone.get(),
#                                             self.entry_email.get()))


# ####################################################
# # Класс БД
# class DB:
#     def __init__(self):
#         self.conn = sqlite3.connect('contacts.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute(''' CREATE TABLE IF NOT EXISTS users(
#                                 ID INTEGER PRIMARY KEY NOT NULL,
#                                 name TEXT,
#                                 phone TEXT,
#                                 email TEXT )''')
#         self.conn.commit()

#     def insert_data (self, name, phone, email):
#         self.cur.execute(''' INSERT INTO users (name, phone, email)
#                          VALUES (?, ?, ?)''', (name, phone, email))
#         self.conn.commit()

# ####################################################
# if __name__ == '__main__':
#     root = tk.Tk()
#     db = DB()
#     app = Main(root)
#     app.pack()
#     root.title('Телефонная книга')
#     root.geometry('645x450')
#     root.resizable(False, False)
#     root.configure(bg = 'White')
#     root.mainloop()
