import sqlite3

conn = sqlite3.connect('db_1')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50),author VARCHAR(50),price DECIMAL(8, 2),amount INTEGER )''')
cursor.execute('''INSERT into tab_1 (title,author,price,amount) VALUES ('qwer','max',11,5)''')
cursor.execute('''INSERT into tab_1 (title,author,price,amount) VALUES ('asd','vlad',8,980)''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
# cursor.execute('''DELETE FROM tab_1''')
# conn.commit()
k = cursor.fetchall()
print(k)


