import sqlite3

conn = sqlite3.connect('db_2')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(title_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_4(num_id INTEGER PRIMARY KEY AUTOINCREMENT, num INTEGER)''')
# cursor.execute('''INSERT into tab_3 (title) VALUES ('qwer')''')
# cursor.execute('''INSERT into tab_4 (num) VALUES (3454)''')
conn.commit()

sp = ['11111', 1, 3, 5, 7, 'sfgdge', '56gd', 88]
for i in sp:
    if isinstance(i, str):
        cursor.execute('''INSERT  into tab_3 (title) VALUES (?)''', (i,))
        conn.commit()
        cursor.execute('''INSERT  into tab_4 (num) VALUES (?)''', (len(i),))
        conn.commit()
    elif isinstance(i,int):
        if i % 2 == 0:
            cursor.execute('''INSERT  into tab_4 (num) VALUES (?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT  into tab_3 (title) VALUES ('нечетное')''')
            conn.commit()

cursor.execute('''SELECT*FROM tab_3''')
q = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_4''')
# cursor.execute('''DELETE FROM tab_3''')
# cursor.execute('''DELETE FROM tab_4''')
# conn.commit()
k = cursor.fetchall()
# q = cursor.fetchall()
print('Таблица 1:', q)
print('Таблица 2:', k)

if len(k) > 5:
    cursor.execute('''DELETE FROM tab_4 WHERE num_id = 226 ''')
    conn.commit()
else:
    cursor.execute('''UPDATE tab_4 SET num = 'hello' WHERE num_id = 227 ''')

cursor.execute('''SELECT*FROM tab_4''')
p = cursor.fetchall()
print('Таблица 3:', p)


