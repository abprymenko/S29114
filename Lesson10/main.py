import sqlite3
conn = sqlite3.connect('itstep.db')
curs = conn.cursor()

#create
#curs.execute('CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)')

#insert
# curs.execute('INSERT INTO students VALUES(1, "Eva", 15, 12)')
# curs.execute('INSERT INTO students VALUES(2, "Uliana", 15, 12)')
# curs.execute('INSERT INTO students VALUES(3, "Bogdan", 14, 12)')
# curs.execute('INSERT INTO students VALUES(4, "Mark", 14, 12)')
# curs.execute('INSERT INTO students VALUES(5, "Boris", 15, 12)')
# curs.execute('INSERT INTO students VALUES(6, "Lev", 14, 12)')
# curs.execute('INSERT INTO students VALUES(7, "Magomed-Saleh", 13, 10)')
# curs.execute('INSERT INTO students VALUES(7, "Magomed-Emin", 14, 12)')
# conn.commit()


#select

curs.execute('SELECT name, age FROM students')
conn.commit()
rows = curs.fetchall()
print(rows)
print(type(rows))
print(type(rows[0]))


curs.close()
conn.close()