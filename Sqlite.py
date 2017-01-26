import sqlite3

connection = sqlite3.connect('example.sqlite')

cursor = connection.cursor()

connection.execute('''
            create table if not exists user (
                id integer primary key autoincrement
                ,username text
                ,title text
            )
            ''')

connection.execute('''
       insert into user (username, title)
       values
       ('steve', 'student'),
       ('vincert', 'student')
       ''')

for row in connection.execute("select * from user"):
    print(row)

connection.close()